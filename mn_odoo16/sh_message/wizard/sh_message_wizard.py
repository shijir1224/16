# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import api, fields, models, _

class sh_message_wizard(models.TransientModel):
    _name="sh.message.wizard"
    
    def get_default(self):
        if self.env.context.get("message",False):
            return self.env.context.get("message")
        return False 

    name=fields.Html(string="Message",readonly=True,default=get_default)
    
    