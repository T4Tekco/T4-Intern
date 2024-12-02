from odoo import fields, models

class CustomerOdoo(models.Model):
    _name = 'customer.odoo'
    _description = 'Khách hàng'

    name = fields.Char(string='Tên khách hàng', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Số điện thoại')
    address = fields.Char(string='Địa chỉ')
    date_of_birth = fields.Date(string='Ngày sinh')
    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác')
    ], string='Giới tính')
    order_ids = fields.One2many('order.odoo', 'customer_id', string='Đơn hàng')
