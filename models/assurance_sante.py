from odoo import models, fields, api, _

class AssuranceSanteCRM(models.Model):
    _inherit = "crm.lead"
    _description = "Custom fields to CRM Lead"
    
    sexe = fields.selection([
        ('homme', 'Homme'), ('femme', 'Femme')])
