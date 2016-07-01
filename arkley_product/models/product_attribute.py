# -*- coding: utf-8 -*-

from openerp import models, fields, api

class product_attribute(models.Model):
    _inherit = "product.attribute"

    type = fields.Selection([('radio', 'Radio'), ('select', 'Select'), ('color', 'Color'), ('hidden', 'Hidden'), ('text', 'Text')], string="Type")