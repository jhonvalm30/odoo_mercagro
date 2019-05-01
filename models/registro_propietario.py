# -*- coding: utf-8 -*-
from odoo import api, fields, models

class registro_propietario(models.Model):
    _name = 'registro.propietario'
    _rec_name = 'name'
    propieatario.id = fields.Integer('ID', required=True)
    cedula = fields.Integer('Cédula', required=True)
    name = fields.Char('Nombre', size=100, required=True)
    telefono = fields.Integer('Telèfono celular', required=True)