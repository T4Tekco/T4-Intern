from odoo import fields, models

class ShippingOdoo(models.Model):
    _name = 'shipping.odoo'
    _description = 'Thông tin vận chuyển'

    payment_id = fields.Many2one('payment.odoo', string='Thanh toán', required=True)
    shipping_address = fields.Char(string='Địa chỉ giao hàng', required=True)
    shipping_date = fields.Date(string='Ngày giao hàng')
    estimated_delivery_date = fields.Date(string='Ngày dự kiến nhận hàng')
    carrier = fields.Char(string='Đơn vị vận chuyển')
    tracking_number = fields.Char(string='Mã vận chuyển')
    status = fields.Selection([
        ('pending', 'Đang xử lý'),
        ('shipped', 'Đã giao'),
        ('delivered', 'Đã nhận'),
        ('returned', 'Đã trả lại')
    ], string='Trạng thái', default='pending')