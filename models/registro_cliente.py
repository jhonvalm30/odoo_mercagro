# -*- coding: utf-8 -*-
from odoo import api, fields, models

class registro_cliente(models.Model):
    _name = 'registro.propietario'
    _rec_name = 'name'
    cliente.id = fields.Integer('ID', required=True)
    cedula = fields.Integer('Cédula', required=True)
    name = fields.Char('Nombre', size=100, required=True)
    telefono = fields.Integer('Telèfono celular', required=True)
    ciudad = fields.Char('Ciudad', size=100, required=True)
    direccion = fields.Char('Dirección', size=100, required=True)