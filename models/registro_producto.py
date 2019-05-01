# -*- coding: utf-8 -*-
from odoo import api, fields, models

class registro_producto(models.Model):
    _name = 'registro.producto'
    _rec_name = 'name'
    producto_id = fields.Integer('ID', required=True)
    name = fields.Char('Nombre producto', size=100, required=True)
    peso = fields.Integer('Peso', required=True)
    fecha_cosecha = fields.Datetime('Fecha de cosecha', default=fields.Date.today, required=True)

