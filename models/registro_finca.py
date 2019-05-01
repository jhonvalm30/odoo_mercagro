# -*- coding: utf-8 -*-
from odoo import api, fields, models

class registro_producto(models.Model):
    _name = 'registro.finca'
    _rec_name = 'name'
    finca_id = fields.Integer('ID', required=True)
    name = fields.Char('Nombre finca', size=100, required=True)
    ubicacion = fields.Char('Ubicaciòn', size=100, required=True)
    lote = fields.Char('Lote (KM)', size=100, required=True)
