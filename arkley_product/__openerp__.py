# -*- coding: utf-8 -*-
{
    'name': "Product Extended",


    'description': """
        Extension of Product module.
    """,

    'author': "Cloud1990",
    'website': "http://www.cloud1990.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/res_partner.xml',
    ],
}