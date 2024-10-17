# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import json
from urllib.parse import urlparse, parse_qs

from odoo.http import request, Response

import requests
from werkzeug import urls
from werkzeug.exceptions import Forbidden
from werkzeug.utils import redirect

from odoo import _, http
from odoo.exceptions import ValidationError
from odoo.tools import html_escape

_logger = logging.getLogger(__name__)


class MainController(http.Controller):


    @http.route('/api/hello', type='http', auth='public', methods=['GET'], csrf=False)
    def hello_world(self):
        return Response("Hello World", content_type='text/plain', status=200)
    
    @http.route('/api/hello-world', type='http', auth='public', methods = ['GET'], csrf=False)
    def hello_worlds(self):
        response_data = {"hello_response": "HelloWorld 2"}
        return Response(json.dumps(response_data), content_type='application/json', status=200)




    @http.route('/courses', type='http', auth="public", website=True)
    def get_courses(self):
        records = http.request.env['course.odoo'].search([])

        return http.request.render(
            "hello_world.course_list_template",

            {"courses": records},
        )
    

  

