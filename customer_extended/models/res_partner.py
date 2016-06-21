# -*- coding: utf-8 -*-

from openerp import models, fields, api

class res_partner(models.Model):
    _inherit = 'res.partner'

    street3 = fields.Char('Address 3')
    est_email = fields.Char('Establishment E-mail')
    est_no = fields.Char('Establishment No')
    est_type = fields.Char('Establishment Type')
    est_desc = fields.Char('Establishment Description')
    contact_id = fields.Char('Contact Id')
    lea_ref = fields.Char('LEA Ref')
    local_auth = fields.Char('Local Authority')
    boarding = fields.Char('Boarding')
    easting = fields.Char('Easting')
    northing = fields.Char('Northing')
    mailsort = fields.Char('Mailsort')
    no_of_boarders = fields.Integer('No of Boarders')
    nursery_unit = fields.Char('Nursery Unit')
    religion = fields.Char('Religion')
    sex = fields.Char('Sex')
    pupils_roll = fields.Char('Pupils Roll')
    lower_age = fields.Char('Lower Age')
    upper_age = fields.Char('Upper Age')
    def_number = fields.Char('DFE Number')


# class customer_extended(models.Model):
#     _name = 'customer_extended.customer_extended'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100