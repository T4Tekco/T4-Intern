from odoo import fields, models

class PaymentOdoo(models.Model):
    _name = 'payment.odoo'
    _description = 'Thanh toán'

    name = fields.Char(string='Mã thanh toán', required=True, default=lambda self: self.env['ir.sequence'].next_by_code('payment.odoo'))
    order_id = fields.Many2one('order.odoo', string='Đơn hàng', required=True)
    payment_date = fields.Date(string='Ngày thanh toán', default=fields.Date.today, required=True)
    amount = fields.Float(string='Số tiền', required=True)
    payment_method = fields.Selection([
        ('cash', 'Tiền mặt'),
        ('bank', 'Chuyển khoản'),
        ('credit_card', 'Thẻ tín dụng')
    ], string='Phương thức thanh toán', required=True)
    status = fields.Selection([
        ('pending', 'Đang chờ'),
        ('completed', 'Hoàn thành'),
        ('failed', 'Thất bại')
    ], string='Trạng thái', default='pending')
    shipping_id = fields.One2many('shipping.odoo', 'payment_id', string='Vận chuyển')
