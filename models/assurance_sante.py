from odoo import api, fields, models, tools, SUPERUSER_ID
from datetime import date, datetime, timedelta

class AssuranceSanteCRM(models.Model):
    _inherit = "crm.lead"
    _description = "Custom fields to CRM Lead"
    
    sexe = fields.Selection([
        ('homme', 'Homme'), ('femme', 'Femme')])
    date_naissance = fields.Date('Date de naissance')
    regime_social = fields.Char('Régime Social')
    date_debut = fields.Date('Date de début de contrat')
    assure = fields.Selection([
        ('vous','Vous'),('couple','Vous et votre conjoint'),('enfants', 'Vous et vos enfants'),('famille','Vous, Votre Conjoint et Vos enfants')
    ])
    date_naissance_conjoint = fields.Date('Date de naissance du Conjoint')
    regime_social_conjoint = fields.Char('Régime Social du Conjoint')
    nbre_enfants = fields.Selection([
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5')
    ])
    date_naissance_enfant1 = fields.Date('Date de naissance - Enfant 1')
    date_naissance_enfant2 = fields.Date('Date de naissance - Enfant 2')
    date_naissance_enfant3 = fields.Date('Date de naissance - Enfant 3')
    date_naissance_enfant4 = fields.Date('Date de naissance - Enfant 4')
    date_naissance_enfant5 = fields.Date('Date de naissance - Enfant 5')
