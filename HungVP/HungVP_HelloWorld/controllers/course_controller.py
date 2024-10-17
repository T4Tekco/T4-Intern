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

            course_data = []
            for course in courses:
                course_data.append({
                    'id': course.id,
                    'name': course.name,
                    'is_active': course.is_active,
                })

            return FormatResponse(200, "Courses retrieved successfully", course_data).to_response()

        except Exception as e:
            _logger.error(f"Error in API GET: {str(e)}")
            return FormatResponse(400, str(e)).to_response()


    @http.route('/api/courses/<int:course_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_course_byId(self, course_id, **kwargs):
        try:
            # Tìm khoá học theo ID
            result_course = request.env['course.odoo'].sudo().search([('id', '=', course_id)], limit=1)

            if not result_course:
                return FormatResponse(404, "Course not found").to_response()

            course_data = {
                'id': result_course.id,
                'name': result_course.name,
                'is_active': result_course.is_active,
            }

            return FormatResponse(200, f'Course found with course_id: {course_id}', course_data).to_response()

        except Exception as e:
            _logger.error(f"Error in API GET: {str(e)}")
            return FormatResponse(400, str(e)).to_response()

    @http.route('/api/courses', type='http', auth='public', methods=['POST'], csrf=False)
    def create_course(self, **kwargs):
        try:
            data = json.loads(request.httprequest.data)
            
            existing_course = request.env['course.odoo'].sudo().search([('name', '=', data.get('name'))], limit=1)
            
            if existing_course:
                course_data = {
                    'id': existing_course.id,
                    'name': existing_course.name,
                    'is_active': existing_course.is_active,
                }
                return FormatResponse(200, 'Course already exists').to_response()
            
            # Tạo khoá học mới
            new_course = request.env['course.odoo'].sudo().create({
                'name': data.get('name'),
                'is_active': data.get('is_active', True),  # Mặc định là True
            })
            
            course_data = {
                'id': new_course.id,
                'name': new_course.name,
                'is_active': new_course.is_active,
            }

            return FormatResponse(201, 'Course created successfully', course_data).to_response()
        
        except Exception as e:
            _logger.error(f"Error in API POST: {str(e)}")
            return FormatResponse(400, str(e)).to_response()

    @http.route('/api/courses/<int:course_id>', type='http', auth='public', methods=['PUT'], csrf=False)
    def update_course(self, course_id, **kwargs):
        try:
            data = json.loads(request.httprequest.data)
            course = request.env['course.odoo'].sudo().search([('id', '=', course_id)], limit=1)

            if not course:
                return FormatResponse(404, 'Course not found').to_response()

            # Cập nhật thông tin khoá học
            course.write({
                'name': data.get('name', course.name),
                'is_active': data.get('is_active', course.is_active),
            })
            
            course_data = {
                'id': course.id,
                'name': course.name,
                'is_active': course.is_active,
            }
            
            return FormatResponse(200, 'Course updated successfully', course_data).to_response()

        except Exception as e:
            _logger.error(f"Error in API PUT: {str(e)}")
            return FormatResponse(400, str(e)).to_response()

    @http.route('/api/courses/<int:course_id>', type='http', auth='public', methods=['DELETE'], csrf=False)
    def delete_course(self, course_id, **kwargs):
        try:
            course = request.env['course.odoo'].sudo().search([('id', '=', course_id)], limit=1)

            if not course:
                return FormatResponse(404, 'Course not found').to_response()

            course.unlink()
            
            return FormatResponse(200, 'Course deleted successfully').to_response()

        except Exception as e:
            _logger.error(f"Error in API DELETE: {str(e)}")
            return FormatResponse(400, str(e)).to_response()
