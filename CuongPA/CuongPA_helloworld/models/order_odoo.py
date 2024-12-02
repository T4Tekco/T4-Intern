from odoo import fields, models

class OrderOdoo(models.Model):
    _name = 'order.odoo'
    _description = 'Đơn hàng'

    name = fields.Char(string='Mã đơn hàng', required=True)
    date_order = fields.Date(string='Ngày đặt hàng', default=fields.Date.today)
    total_amount = fields.Float(string='Tổng tiền', store=True)
    customer_id = fields.Many2one('customer.odoo', string='Khách hàng', required=True)
    product_ids = fields.Many2many('product.odoo', string='Sản phẩm')
    delivery_address = fields.Char(string='Địa chỉ giao hàng')
    payment_method = fields.Selection([
        ('cash', 'Tiền mặt'),
        ('bank', 'Chuyển khoản')
    ], string='Phương thức thanh toán')
    
    status = fields.Selection([
        ('draft', 'Bản nháp'),
        ('confirmed', 'Đã xác nhận'),
        ('done', 'Hoàn thành'),
        ('cancel', 'Hủy')
    ], string='Trạng thái', default='draft')

    # Liên kết đến bảng payment_odoo và shipping_odoo
    payment_ids = fields.One2many('payment.odoo', 'order_id', string='Thanh toán')
    

    def create(self, vals):
        order = super(OrderOdoo, self).create(vals)
        order._compute_total_amount()
        return order

    def write(self, vals):
        result = super(OrderOdoo, self).write(vals)
        if 'product_ids' in vals:
            self._compute_total_amount()
        return result

    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(product.price for product in order.product_ids)
