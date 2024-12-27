from odoo import fields, models

class ProductOdoo(models.Model):
    _name = 'product.odoo'
    _description = 'Sản phẩm'

    name = fields.Char(string='Tên sản phẩm', required=True)
    price = fields.Monetary(string='Giá sản phẩm')
    currency_id = fields.Many2one('res.currency', string='Đơn vị tiền tệ', default=lambda self: self.env.ref('base.VND').id)
    description = fields.Text(string='Mô tả')
    category = fields.Selection([
        ('clothing', 'Quần áo'),
        ('bags', 'Túi xách'),
        ('footwear', 'Giày dép')
    ], string='Danh mục', required=True)
    stock = fields.Integer(string='Số lượng tồn kho')
    image = fields.Image(string='Ảnh sản phẩm')  
