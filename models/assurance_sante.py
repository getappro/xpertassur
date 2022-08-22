from odoo import api, fields, models, tools, SUPERUSER_ID

class AssuranceSanteCRM(models.Model):
    _inherit = "crm.lead"
    _description = "Custom fields to CRM Lead"
    
    sexe = fields.Selection([
        ('homme', 'Homme'), ('femme', 'Femme')])
