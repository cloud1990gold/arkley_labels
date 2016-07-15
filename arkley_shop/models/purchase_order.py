from openerp import api, models, fields, api, _
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT

class purchase_order_line(models.Model):
	_inherit = 'purchase.order.line'

	customised_image = fields.Binary(
			string='Customised Image',
			required=False,
			readonly=True,
	)

	customised_image_filename = fields.Char(
			default="image.png",
	)

	@api.multi
	def write(self, vals):
		ir_attachment_obj = self.env['ir.attachment']
		product_obj = self.env['product.product']
		for rec in self:
			if vals.get('customised_image'):
				attachment_vals = {
					'res_model': 'purchase.order',
					'res_id': rec.order_id,
					'type': 'binary',
					'datas': vals.get('customised_image'),
					'name': rec.product_id.name,
					'store_fname': rec.product_id.name + '.jpg',
					'datas_fname': rec.product_id.name + '.jpg'
				}
				ir_attachment_obj.create(attachment_vals)
		return True


class ProcurementOrder(models.Model):
    _inherit = 'procurement.order'

    @api.multi
    def make_po(self):
	    cache = {}
	    res = []
	    for procurement in self:
		    suppliers = procurement.product_id.seller_ids.filtered(
			    lambda r: not r.product_id or r.product_id == procurement.product_id)
		    if not suppliers:
			    procurement.message_post(
				    body=_('No vendor associated to product %s. Please set one to fix this procurement.') % (
				    procurement.product_id.name))
			    continue
		    supplier = suppliers[0]
		    partner = supplier.name

		    gpo = procurement.rule_id.group_propagation_option
		    group = (gpo == 'fixed' and procurement.rule_id.group_id) or \
		            (gpo == 'propagate' and procurement.group_id) or False

		    domain = (
			    ('partner_id', '=', partner.id),
			    ('state', '=', 'draft'),
			    ('picking_type_id', '=', procurement.rule_id.picking_type_id.id),
			    ('company_id', '=', procurement.company_id.id),
			    ('dest_address_id', '=', procurement.partner_dest_id.id))
		    if group:
			    domain += (('group_id', '=', group.id),)

		    if domain in cache:
			    po = cache[domain]
		    else:
			    po = self.env['purchase.order'].search([dom for dom in domain])
			    po = po[0] if po else False
			    cache[domain] = po
		    if not po:
			    vals = procurement._prepare_purchase_order(partner)
			    po = self.env['purchase.order'].create(vals)
			    cache[domain] = po
		    elif not po.origin or procurement.origin not in po.origin.split(', '):
			    # Keep track of all procurements
			    if po.origin:
				    if procurement.origin:
					    po.write({'origin': po.origin + ', ' + procurement.origin})
				    else:
					    po.write({'origin': po.origin})
			    else:
				    po.write({'origin': procurement.origin})
		    if po:
			    res += [procurement.id]

		    # Create Line
		    po_line = False
		    for line in po.order_line:
			    if line.product_id == procurement.product_id and line.product_uom == procurement.product_id.uom_po_id:
				    procurement_uom_po_qty = self.env['product.uom']._compute_qty_obj(procurement.product_uom,
				                                                                      procurement.product_qty,
				                                                                      procurement.product_id.uom_po_id)
				    seller = self.product_id._select_seller(
						    procurement.product_id,
						    partner_id=partner,
						    quantity=line.product_qty + procurement_uom_po_qty,
						    date=po.date_order and po.date_order[:10],
						    uom_id=procurement.product_id.uom_po_id)

				    price_unit = self.env['account.tax']._fix_tax_included_price(seller.price,
				                                                                 line.product_id.supplier_taxes_id,
				                                                                 line.taxes_id) if seller else 0.0
				    if price_unit and seller and po.currency_id and seller.currency_id != po.currency_id:
					    price_unit = seller.currency_id.compute(price_unit, po.currency_id)

				    po_line = line.write({
					    'product_qty'    : line.product_qty + procurement_uom_po_qty,
					    'price_unit'     : price_unit,
					    'procurement_ids': [(4, procurement.id)]
				    })
				    break
		    if not po_line:
			    vals = procurement._prepare_purchase_order_line(po, supplier)
			    print "----------",procurement.sale_line_id

			    self.env['purchase.order.line'].create(vals)
	    return res