# -*- coding: utf-8 -*-
from odoo import http

# class InventoryMenitem(http.Controller):
#     @http.route('/inventory_menitem/inventory_menitem/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventory_menitem/inventory_menitem/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventory_menitem.listing', {
#             'root': '/inventory_menitem/inventory_menitem',
#             'objects': http.request.env['inventory_menitem.inventory_menitem'].search([]),
#         })

#     @http.route('/inventory_menitem/inventory_menitem/objects/<model("inventory_menitem.inventory_menitem"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventory_menitem.object', {
#             'object': obj
#         })