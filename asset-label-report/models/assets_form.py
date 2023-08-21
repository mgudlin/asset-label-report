from odoo import fields, models


class AccountAsset(models.Model):
    _inherit = 'account.asset'

    broj_osn_sred = fields.Char(string='Broj Osn. Sredstva')