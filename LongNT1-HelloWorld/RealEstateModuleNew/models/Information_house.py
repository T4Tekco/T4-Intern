from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)
import json
class Product(models.Model):
    
    _inherit = 'product.template'
    

    # product_type_id = fields.Many2one("product.type.new", string="Loại bất động sản")

    product_type_id = fields.Many2one("category.bds", string="Loại bất động sản")
    nums_bedrooms = fields.Integer(string="Số phòng ngủ")
    nums_bath = fields.Integer(string="Số nhà vệ sinh")
    facade = fields.Float(string="Mặt tiền (m)")
    real_length = fields.Float(string="Chiều dài (m)")
    way_in = fields.Integer(string="Ngõ vào (m)")
    floors = fields.Integer(string="Số Tầng")
    interior = fields.Char(string="Nội thất")
    direction_id = fields.Many2one("product.direction.new", string="Hướng nhà")

    acreage = fields.Float(string="Diện tích")
    real_acreage = fields.Float(string="Diện tích thực tế")
    alley = fields.Char(string="Ngõ, số nhà")
    street = fields.Char(string="Đường phố")
    ward = fields.Char(string="Phường xã")
    district = fields.Char(string="Quận huyện")
    city = fields.Char(string="Thành phố")
    state_id = fields.Many2one(comodel_name="res.country.state")
    country_id = fields.Many2one(
        comodel_name="res.country", default=lambda self: self.env.ref("base.vn")
    )


    sell_name = fields.Char(string="Tên chủ nhà", )
    sell_phone = fields.Char(string="Điện thoại chủ nhà", )



    offer_price = fields.Float(string="Giá chào hợp đồng (Triệu VND)")
    close_price = fields.Float(string="Giá chốt (Triệu VND)")
    bonus_money_percent = fields.Float(string="Hoa hồng %")
    bonus_money = fields.Float(string="Hoa hồng (Triệu VND)")



    district_id = fields.Many2one("res.country.district_new", string="District")
    ward_id = fields.Many2one("res.country.ward_new", string="Ward")

    @api.onchange("state_id")
    def _onchange_state_id(self):
        self.district_id = False
        self.ward_id = False

    @api.onchange("district_id")
    def _onchange_district_id(self):
        self.ward_id = False

    # Tài khoản liên kết
    supp_ggmap = fields.Char(string="Google Map")
    
    multiple_images = fields.Many2many('ir.attachment', 
        'product_template_ir_attachment_rel_multiple',  # Bảng trung gian tùy chỉnh
        'product_id', 'attachment_id',string="Ảnh sổ đỏ",help="Chọn nhiều hình ảnh cho sản phẩm này",
        groups='RealEstateModuleNew.group_people_dauchu',domain=[('mimetype', 'ilike', 'image')],)
    
    
    additional_images_2 = fields.Many2many(
        'ir.attachment', 
        'product_template_ir_attachment_rel_additional_2',  # Bảng trung gian khác nữa
        'product_id', 'attachment_id', 
        string="Hình ảnh chi tiết",
        help="Chọn thêm hình ảnh chi tiết",
        groups='RealEstateModuleNew.group_people_dauchu',
        domain=[('mimetype', 'ilike', 'image')],
    )

    # image_chitetnha = fields.Many2many('ir.attachment', 
    #     'product_template_ir_attachment_rel_image_chitetnha',  # Bảng trung gian khác nữa
    #     'product_id', 'attachment_id', 
    #     string="Ảnh chi tiết nhà",
    #     help="Có thể chọn thêm hình ảnh",
    #     groups='RealEstateModuleNew.group_people_dauchu',
    #     required=True,
    #     domain=[('mimetype', 'ilike', 'image')],
    # )
    # image_hopdong = fields.Many2many('ir.attachment', 
    #     'product_template_ir_attachment_rel_image_hopdong',  # Bảng trung gian khác nữa
    #     'product_id', 'attachment_id', 
    #     string="Ảnh hợp đồng",
    #     help="Có thể chọn thêm hình ảnh",
    #     groups='RealEstateModuleNew.group_people_dauchu',
    #     required=True,
    #     domain=[('mimetype', 'ilike', 'image')],
    # )

    
    
    # def write(self, vals):
    #     _logger.info(vals)  
    #     new_record = super(Product, self).write(vals)
    #     return new_record


    # multi_images = fields.Many2many(
    #     'ir.attachment', 
    #     string="Images",
    #     help="Upload multiple images for the product", groups='RealEstateModuleNew.group_people_dauchu')
    

    #người chờ duyệt
    follower_ids = fields.Many2many('product.follow', 'product_id', string="Followers")
    isFollow = fields.Boolean(compute='_compute_is_follow', string="Is Follow")
    isApprove = fields.Boolean(compute='_compute_is_approve', string="Is Follow")
    isReadonly = fields.Boolean(string="Is Readonly")

    #Nguoi duoc duyệt
    follower_2_ids = fields.Many2many('product.follow', 'product_id_2', string="Followers")
    #follower_2_ids = fields.Many2many('product.follow', 'product_id', string="Followers")

   

    
    def _compute_is_approve(self):
        for record in self:
            if record.env.user.has_group('RealEstateModuleNew.group_people_dauchu'):
                record.isReadonly = False
            else:
                record.isReadonly = True

            if record.env.user in record.follower_2_ids.user_id or record.env.user.has_group('RealEstateModuleNew.group_people_dauchu') or record.env.user.has_group('RealEstateModuleNew.group_people_chunha'):
                record.isApprove = True
            else:
                record.isApprove = False    
    def _compute_is_follow(self):
        for record in self:
            record.isFollow = record.env.user in record.follower_ids.user_id
    def action_follow_product(self):
        # Phương thức này sẽ được gọi từ UI, có thể nhận thêm đối số
        self.ensure_one()  # Đảm bảo chỉ có một bản ghi

        # Kiểm tra xem người dùng đã theo dõi sản phẩm chưa
        existing_follow = self.env['product.follow'].search([
            ('user_id', '=', self.env.user.id),
            ('product_id', '=', self.id)
        ], limit=1)
        _logger.info(existing_follow)


        if not existing_follow:
            existing_follow = self.env['product.follow'].create({
                'user_id': self.env.user.id,
                'product_id': self.id,
                'product_id_2': self.id
            })
            _logger.info("fff")
        
        self.follower_ids = [(4, existing_follow.id)]    


        
        
        #Gửi thông báo đến tài khoản đầu khách
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
            # 'params': {
            #  'title': 'Thông báo',
            # 'message': 'Hãy đợi Đầu chủ duyệt yêu cầu của bạn!',
            #  'sticky': False,
            # },
        }
        
    def write(self, vals):
        _logger.info(vals)  
        {'follower_ids': [[3, 1]]}
        new_record = super(Product, self).write(vals)
        return new_record
    


    def domain(self):
            # Tạo mảng để lưu trữ các ID của các đối tác liên quan (partner_ids).
        _logger.info([self.env.user.id])
        if self.env.user.has_group('RealEstateModuleNew.group_people_dauchu'):
            return []
        return [('user_id_ban', '=', self.env.user.id)]
    #tạo sản phẩm bán
    sale_product_ids = fields.One2many('sale.product', 'product_template_id', string="Sản phẩm bán",domain=domain)

    
    def action_create_sale_product(self):
        self.ensure_one()
        sale_product = self.env['sale.product'].create({
            'product_template_id': self.id,
            'product_type_id': self.product_type_id.id,
            'nums_bedrooms': self.nums_bedrooms,
            'nums_bath': self.nums_bath,
            'facade': self.facade,
            'real_length': self.real_length,
            'way_in': self.way_in,
            'floors': self.floors,
            'interior': self.interior,
            'direction_id': self.direction_id.id,
            'acreage': self.acreage,
            'real_acreage': self.real_acreage,
            'alley': self.alley,
            'street': self.street,
            'ward': self.ward,
            'district': self.district,
            'city': self.city,
            'state_id': self.state_id.id,
            'country_id': self.country_id.id,
            'sell_name': self.sell_name,
            'sell_phone': self.sell_phone,
            'offer_price': self.offer_price,
            'close_price': self.close_price,
            'bonus_money_percent': self.bonus_money_percent,
            'bonus_money': self.bonus_money,
            'district_id': self.district_id.id,
            'ward_id': self.ward_id.id,
            'supp_ggmap': self.supp_ggmap,
            # Có thể thêm các trường khác nếu cần
        })
        return {
            'type': 'ir.actions.act_window',
            'name': 'Thông tin bán',
            'res_model': 'sale.product',
            'res_id': sale_product.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'current',
        }
    
    # sale_product_ids = fields.One2many('sale.product', 'product_template_id', string="Sản phẩm bán")

    # def action_create_sale_product(self):
        
    #     self.ensure_one()
    #     sale_product = self.env['sale.product'].create({
    #         'product_template_id': self.id,
            
    #         # Có thể thêm các trường khác nếu cần
    #     })
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Thông tin bán',
    #         'res_model': 'sale.product',
    #         'res_id': sale_product.id,
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'target': 'current',
    #     }
    
        
