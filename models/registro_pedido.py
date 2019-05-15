# -*- coding: utf-8 -*-
from openerp import api, fields, models
from . import registro_cliente, registro_finca, registro_producto

class registro_pedido(models.Model):
    _name = 'registro.pedido'
    _rec_name = 'name'
    name = fields.Many2one('registro.finca', 'Finca donde sale el prouducto', select=True, track_visibility='onchange')
    cliente_id = fields.Many2one('registro.cliente', 'Cliente', select=True, track_visibility='onchange')
    prouducto_id = fields.Many2one('registro.producto', 'Producto', select=True, track_visibility='onchange')
    autorizado = fields.Boolean('¿Salida Autorizada?', default=False, required=True)
    fecha_salida = fields.Datetime('Fecha Salida', default=fields.Date.today, required=True)