# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class addFieldDiference(models.Model):

	_inherit = 'stock.inventory.line'

	diference_stock = fields.Float( string = 'Diferencia', store=True )

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
	field_ses = fields.Many2one('pos.session', string = 'Session')
	field_con = fields.Many2one('pos.config', string = 'Config', required = True)

	@api.onchange('field_con')
	def _val_sesion(self):
		if self.field_con:
			busq = self.env['pos.session'].search([('config_id','=', self.field_con.id)], limit = 1)
			self.field_ses = busq.id

	@api.one
	def valid_diference(self):
		compr = False
		price_amount = 0
		self.valid_dif = True
		for record in self.line_ids:
			if record:
				for line in record:
					oper = line.product_qty - line.theoretical_qty
					line.diference_stock = oper
					if line.diference_stock > 0:
						compr = True
						price_amount += line.product_id.list_price * line.diference_stock
		if compr == True:
			ped_vent = self.env['pos.order']
			ped_values = {
				'name' : self.name,
				'company_id' : self.company_id.id,
				'user_id' : self.env.user.id,
				'amount_tax' : 0.0,
				'amount_total' : price_amount,
				'amount_paid' : 0,
				'amount_return' : 0,
				'partner_id' : self.env.user.id,
				'sequence_number' : 1,
				'session_id' : self.field_ses.id,
				'state' : 'draft',
				'location_id' : self.location_id.id,
			}
			ped_id = ped_vent.create(ped_values)
			ped_ord_line = self.env['pos.order.line']
			for record in self.line_ids:
				if record:
					for line in record:
						if line.diference_stock > 0:
							list_dat = {
								'company_id' : self.company_id.id,
								'product_id' : line.product_id.id,
								'qty' : line.diference_stock,
								'price_unit' : line.product_id.list_price,
								'discount' : 0,
								'price_subtotal' : line.product_id.list_price * line.diference_stock,
								'price_subtotal_incl' : line.product_id.list_price * line.diference_stock,
								'order_id' : ped_id.id
							}
							ped_ord = ped_ord_line.create(list_dat)
		else:
			raise UserError('No hay productos con diferencia, para crear un pedido de venta')







		