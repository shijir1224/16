# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class Company(models.Model):
    _inherit = 'res.company'
    
    portal_confirmation_sign = fields.Boolean(string="Online Signature", default=True)
    portal_confirmation_director_sign = fields.Boolean(string="Online Signature", default=True)