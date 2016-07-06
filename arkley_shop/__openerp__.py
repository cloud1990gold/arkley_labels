# -*- coding: utf-8 -*-
{
    'name': "Arkley Shop",


    'description': """
        Extension of Product module.
    """,

    'author': "Cloud1990",
    'website': "http://www.cloud1990.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Ecommerce',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website_sale_product_customise'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template.xml',
        'views/purchase_order.xml',
    ],
}