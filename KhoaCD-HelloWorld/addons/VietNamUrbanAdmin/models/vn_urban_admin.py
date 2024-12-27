from odoo import models, fields, api

class City(models.Model):
    _name = 'res.city'
    _description = 'City'

    name = fields.Char(string='City Name', required=True)
    code = fields.Char(string='City Code', required=True)
    district_ids = fields.One2many('res.district', 'city_id', string='Districts')

class District(models.Model):
    _name = 'res.district'
    _description = 'District'

    name = fields.Char(string='District Name', required=True)
    code = fields.Char(string='District Code', required=True)
    city_id = fields.Many2one('res.city', string='City', required=True)
    ward_ids = fields.One2many('res.ward', 'district_id', string='Wards')

class Ward(models.Model):
    _name = 'res.ward'
    _description = 'Ward'

    name = fields.Char(string='Ward Name', required=True)
    code = fields.Char(string='Ward Code', required=True)
    district_id = fields.Many2one('res.district', string='District', required=True)
