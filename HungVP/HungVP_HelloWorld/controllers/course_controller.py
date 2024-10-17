import logging
import json
from datetime import datetime
from odoo.http import request, Response
from odoo import http
from ..models.format_response import FormatResponse

_logger = logging.getLogger(__name__)

class CourseController(http.Controller):

    @http.route('/api/courses', type='http', auth='public', methods=['GET'], csrf=False)
    def get_all_courses(self, **kwargs):
        try:

            courses = request.env['course.odoo'].sudo().search([])

            _logger.info(f"Number of courses found: {len(courses)}")

            courses_data = []   
            for course in courses:
                courses_data.append({
                    'id': course.id,
                    'name': course.name,
                    'is_active': course.is_avtive,
                })
            
            return FormatResponse(200, "Course retrieved successfully", courses_data).to_response()

        except Exception as e:
            _logger.error(f"Error in API GET: {str(e)}")
            return FormatResponse(400, str(e)).to_response()
        

    @http.route('/api/courses', type='http', auth='public', methods=['POST'], csrf=False)
    def create_course(self, *kwargs):
        
        try:
            data = json.loads(request.httprequest.data)

            existing_course = request.env['course.odoo'].sudo().search([('name', '=', data.get('name'))], limit=1)

            if existing_course:

                course_data = {
                    'id': existing_course.id,
                    'name': existing_course.name,
                    'is_active': existing_course.is_active,
                }
                return FormatResponse(200, 'Course already exists', course_data).to_response()
            
            new_course = request.env['course.odoo'].sudo().create({
                'name': data.get('name'),
                "is_active": data.get('is_active', True),
            })

            return FormatResponse(201, 'Cours create successfully', new_course).to_response()
        
        except Exception as e:
            _logger.error(f"Error in API POST: {str(e)}")
            return FormatResponse(400, str(e)).to_response()
            
        
    