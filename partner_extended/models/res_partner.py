from openerp import api, models, fields

class res_partner(models.Model):

    'state_id': fields.many2one("res.country.state", 'County', ondelete='restrict'),
    'zip': fields.char('Postcode', size=24, change_default=True),