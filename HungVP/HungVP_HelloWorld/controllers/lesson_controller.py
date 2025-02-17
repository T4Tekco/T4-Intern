import logging
import json
from datetime import datetime
from odoo.http import request, Response
from odoo import http
from ..models.format_response import FormatResponse

_logger = logging.getLogger(__name__)

class LessonController(http.Controller):

    @http.route('/api/lessons', type='http', auth='public', methods=['GET'], csrf=False)
    def get_all_lessons(self, **kwargs):
        try:
            lessons = request.env['lesson.odoo'].sudo().search([])

            _logger.info(f"Number of lessons found: {len(lessons)}")

            # Tạo danh sách để lưu kết quả
            lesson_data = []
            for lesson in lessons:
                lesson_data.append({
                    'id': lesson.id,
                    'name': lesson.name,
                    'is_active': lesson.is_active,
                })

            return FormatResponse(200, "Lessons retrieved successfully", lesson_data).to_response()

        except Exception as e:
            _logger.error(f"Error in API GET: {str(e)}")
            return FormatResponse(400, str(e)).to_response()
        
    
    @http.route('/api/lessons/<int:lesson_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_lesson_byId(self, lesson_id, **kwargs):
        try:
            # Tìm bài học theo ID
            existed_lesson = request.env['lesson.odoo'].sudo().search([('id', '=', lesson_id)], limit=1)

            if not existed_lesson:
                return FormatResponse(404, 'Lesson not found').to_response()

            # Chuyển dữ liệu bài học thành dictionary
            lesson_data = {
                'id': existed_lesson.id,
                'name': existed_lesson.name,
                'is_active': existed_lesson.is_active
            }

            return FormatResponse(200, 'Lesson retrieved successfully', lesson_data).to_response()

        except Exception as e:
            _logger.error(f"Error in API GET: {str(e)}")
            return FormatResponse(400, str(e)).to_response()
        
        
    @http.route('/api/lessons', type='http', auth='public', methods=['POST'], csrf=False)
    def create_lesson(self, **kwargs):
        try:
            data = json.loads(request.httprequest.data)
            
            existing_lesson = request.env['lesson.odoo'].sudo().search([('name', '=', data.get('name'))], limit=1)
            
            if existing_lesson:
                lesson_data = {
                    'id': existing_lesson.id,
                    'name': existing_lesson.name,
                    'is_active': existing_lesson.is_active,
                }
                return FormatResponse(200, 'Lesson already exists', lesson_data).to_response()
            
            new_lesson = request.env['lesson.odoo'].sudo().create({
                'name': data.get('name'),
                'is_active': data.get('is_active', True),
            })
            
            new_lesson_data = {
                'id': new_lesson.id,
                'name': new_lesson.name,
                'is_active': new_lesson.is_active,
            }
            
            return FormatResponse(201, 'Lesson created successfully', new_lesson_data).to_response()
        
        except Exception as e:
            _logger.error(f"Error in API POST: {str(e)}")
            return FormatResponse(400, str(e)).to_response()

    @http.route('/api/lessons/<int:lesson_id>', type='http', auth='public', methods=['PUT'], csrf=False)
    def update_lesson(self, lesson_id, **kwargs):
        try:
            data = json.loads(request.httprequest.data)
            lesson = request.env['lesson.odoo'].sudo().search([('id', '=', lesson_id)], limit=1)

            if not lesson:
                return FormatResponse(404, 'Lesson not found').to_response()

            # Update
            lesson.write({
                'name': data.get('name', lesson.name),
                'is_active': data.get('is_active', lesson.is_active),
            })
            
            lesson_data = {
                'id': lesson.id,
                'name': lesson.name,
                'is_active': lesson.is_active,
            }
            
            return FormatResponse(200, 'Lesson updated successfully', lesson_data).to_response()
        
        except Exception as e:
            _logger.error(f"Error in API PUT: {str(e)}")
            return FormatResponse(400, str(e)).to_response()

    @http.route('/api/lessons/<int:lesson_id>', type='http', auth='public', methods=['DELETE'], csrf=False)
    def delete_lesson(self, lesson_id, **kwargs):
        try:
            # Tìm bài học theo ID
            lesson = request.env['lesson.odoo'].sudo().search([('id', '=', lesson_id)], limit=1)

            if not lesson:
                return FormatResponse(404, 'Lesson not found').to_response()

            lesson.unlink()
            
            return FormatResponse(200, 'Lesson deleted successfully').to_response()

        except Exception as e:
            _logger.error(f"Error in API DELETE: {str(e)}")
            return FormatResponse(400, str(e)).to_response()
