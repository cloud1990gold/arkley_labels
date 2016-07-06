from openerp import api, models, fields, _

class sale_order(models.Model):
	_inherit = 'sale.order'

	@api.model
	def _prepare_purchase_order_line_data(self, so_line, date_order, purchase_id, company):
		""" Generate purchase order line values, from the SO line
			:param so_line : origin SO line
			:rtype so_line : sale.order.line record
			:param date_order : the date of the orgin SO
			:param purchase_id : the id of the purchase order
			:param company : the company in which the PO line will be created
			:rtype company : res.company record
		"""
		# price on PO so_line should be so_line - discount
		price = so_line.price_unit - (so_line.price_unit * (so_line.discount / 100))

		# computing Default taxes of so_line. It may not affect because of parallel company relation
		taxes = so_line.tax_id
		if so_line.product_id:
			taxes = so_line.product_id.supplier_taxes_id

		# fetch taxes by company not by inter-company user
		company_taxes = [tax_rec.id for tax_rec in taxes if tax_rec.company_id.id == company.id]
		return {
			'name'        : so_line.name,
			'order_id'    : purchase_id,
			'product_qty' : so_line.product_uom_qty,
			'product_id'  : so_line.product_id and so_line.product_id.id or False,
			'product_uom' : so_line.product_id and so_line.product_id.uom_po_id.id or so_line.product_uom.id,
			'price_unit'  : price or 0.0,
			'company_id'  : so_line.order_id.company_id.id,
			'date_planned': so_line.order_id.commitment_date or date_order,
			'taxes_id'    : [(6, 0, company_taxes)],
			'customised_image': so_line.customised_image,
		}