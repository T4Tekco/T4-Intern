
# from odoo import models, fields, api


# class LongNT1-HelloWorld(models.Model):
#     _name = 'LongNT1-HelloWorld.LongNT1-HelloWorld'
#     _description = 'LongNT1-HelloWorld.LongNT1-HelloWorld'
#     _inherit = 'mail.thread'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

