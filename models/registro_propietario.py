# -*- coding: utf-8 -*-
from odoo import api, fields, models

class registro_propietario(models.Model):
    _name = 'registro.propietario'
    _rec_name = 'name'
    propietario_id = fields.Integer('ID', required=True)
    cedula = fields.Char('Cédula', required=True)
    name = fields.Char('Nombre', required=True)
    telefono = fields.Char('Teléfono celular', required=True)
    _sql_constraints = [('cedula_uniq', 'unique(cedula)', 'El número de identificación debe ser único.')]