import logging
import json
from odoo.http import request

_logger = logging.getLogger(__name__)

class ProductController(http.Controller):
    @http.route('api/product',type='http', auth='public', methods=['GET'], csrf=False)
    def post_product(self):
        args = request.httpprequest.data.decode()
        vals = json.load(args)
        res  = request.env['product'].sudo().create(vals)
        if res:
            return request.make_json_response({
                "message": "Product has been created successfuly"
            }, status=200)
    
    @http.route("api/product/json", methods=["POST"], type="http", auth="none", csrf=False)
    def post_product_json(self):
        args = request.httpprequest.data.decode()
        vals = json.load(args)
        print(vals)