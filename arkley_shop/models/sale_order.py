from openerp import api, models, fields, _

class sale_order(models.Model):
	_inherit = 'sale.order'

	purchase_order_id = fields.Many2one('purchase.order', 'Purchase Order')

	@api.multi
	def write(self, vals):
		purchase_order_line_obj = self.env['purchase.order.line']
		if vals.get('purchase_order_id'):
			for rec in self:
				for line in rec.order_line:
					purchase_line_ids = purchase_order_line_obj.search([('order_id', '=', vals.get('purchase_order_id')),
																		('product_id', '=', line.product_id.id)
																		])
					if purchase_line_ids:
						purchase_line_ids.write({'customised_image': line.customised_image})
		return super(sale_order, self).write(vals)
