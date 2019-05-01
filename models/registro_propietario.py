# -*- coding: utf-8 -*-
from odoo import api, fields, models

class registro_propietario(models.Model):
    _name = 'registro.propietario'
    _rec_name = 'name'
    propietario_id = fields.Integer('ID', required=True)
    cedula = fields.Integer('Cédula', required=True)
    name = fields.Char('Nombre', required=True)
    telefono = fields.Integer('Teléfono celular', required=True)