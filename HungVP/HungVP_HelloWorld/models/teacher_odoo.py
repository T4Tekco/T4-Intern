# -*- coding: utf-8 -*-
from odoo import _, fields, models

class TeacherOdoo(models.Model):
    _name = 'teacher.odoo'  # External ID cho model Teacher
    _description = 'Thông tin giáo viên'

    name = fields.Char(string='Tên giáo viên', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Số điện thoại')
    subject = fields.Char(string='Môn học')
    is_active = fields.Boolean(string='Kích hoạt', default=True)
    course_ids = fields.Many2many(comodel_name='course.odoo', string='Khoá học')

    def toggle_active(self):
        for teacher in self:
            teacher.is_active = not teacher.is_active
