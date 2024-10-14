from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)
class Product(models.Model):
    
    _inherit = 'product.template'
    

    # product_type_id = fields.Many2one("product.type.new", string="Loại bất động sản")

    product_type_id = fields.Many2one("category.bds", string="Loại bất động sản")

    # product_type_id = fields.Char( string="Loại bất động sản")
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
    #is_owner = fields.Boolean(string="Sản phẩm đầu chủ", default=True, readonly=True)
    #juridical = fields.Text(string="Pháp lý")
    alley = fields.Char(string="Ngõ, số nhà",groups='RealEstateModuleNew.group_people_dauchu')
    street = fields.Char(string="Đường phố")
    #street2 = fields.Char(string="Đường phố 2")
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
    # supp_fb = fields.Char(string="Facebook")
    # supp_zl = fields.Char(string="Zalo")
    # supp_wa = fields.Char(string="WhatApp")
    # supp_vb = fields.Char(string="Viber")
    # supp_ms = fields.Char(string="Messenger")
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
    

    #người cho duyet
    follower_ids = fields.Many2many('product.follow', 'product_id', string="Followers")
    isFollow = fields.Boolean(compute='_compute_is_follow', string="Is Follow")
    isApprove = fields.Boolean(compute='_compute_is_approve', string="Is Follow")
    isReadonly = fields.Boolean(string="Is Readonly")

    #Nguoi duoc duyet
    follower_2_ids = fields.Many2many('product.follow', 'product_id_2', string="Followers")
    #follower_2_ids = fields.Many2many('product.follow', 'product_id', string="Followers")
    
    def _compute_is_approve(self):
        for record in self:
            if record.env.user.has_group('RealEstateModuleNew.group_people_dauchu'):
                record.isReadonly = False
            else:
                record.isReadonly = True

            if record.env.user in record.follower_2_ids.user_id or record.env.user.has_group('RealEstateModuleNew.group_people_dauchu'):
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

        if not existing_follow:
            product_follow = self.env['product.follow'].create({
                'user_id': self.env.user.id,
                'product_id': self.id,
                'product_id_2': self.id
            })
            self.follower_ids = [(4, product_follow.id)]    


        
        
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
    