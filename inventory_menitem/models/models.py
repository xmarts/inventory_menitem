# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class addFieldDiference(models.Model):

	_inherit = 'stock.inventory.line'

	diference_stock = fields.Float( string = 'Diferencia', compute='_cal_diference', store=True )

	'''@api.one
	@api.depends('product_qty','theoretical_qty')
	def _cal_diference(self):
		for record in self.inventory_id.line_ids:
			if record:
				for line in record:
					oper = line.product_qty - line.theoretical_qty
					line.diference_stock = oper'''

class addValidDif(models.Model):

	_inherit = 'stock.inventory'

	valid_dif = fields.Boolean( default = False, string = 'Valid' )

	@api.one
	def valid_diference(self):
		self.valid_dif = True
		for record in self.line_ids:
			if record:
				for line in record:
					oper = line.product_qty - line.theoretical_qty
					line.diference_stock = oper







		