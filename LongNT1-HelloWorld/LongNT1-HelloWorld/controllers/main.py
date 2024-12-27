# import logging
# import json
# from urllib.parse import urlparse, parse_qs

# import requests
# from werkzeug import urls
# from werkzeug.exceptions import Forbidden
# from werkzeug.utils import redirect

from odoo import _, http
# from odoo.exceptions import ValidationError
# from odoo.tools import html_escape

# _logger = logging.getLogger(__name__)


class MainController(http.Controller):
    @http.route('/course', type='http', auth="user", website=True)
    def get_courses(self):
        records = http.request.env['course.odoo'].search([])

        return http.request.render(
            # Tên templae (Khởi tạo trong views folder)
            "odoo-config-template-module.course_list_template",
             # Object render
            ## Biến đầu tên là tên biến sẽ gọi trong template
            ## Biến thứ 2   là biến đã query ở trên
            {"course:": records},
        )