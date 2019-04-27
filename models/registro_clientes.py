# -*- coding: utf-8 -*-
from odoo import api, fields, models

class registroclientes_cedula(models.Model):
    _name='registroclientes_cedula'
    _rec_name='name'
    name = fields.Char('Número de identificación', size=20, required=True)

