from openerp import api, models, fields, api, _

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