# -*- coding: utf-8 -*-
from openerp import http

# class CustomerExtended(http.Controller):
#     @http.route('/customer_extended/customer_extended/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_extended/customer_extended/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_extended.listing', {
#             'root': '/customer_extended/customer_extended',
#             'objects': http.request.env['customer_extended.customer_extended'].search([]),
#         })

#     @http.route('/customer_extended/customer_extended/objects/<model("customer_extended.customer_extended"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_extended.object', {
#             'object': obj
#         })