import logging
import json
from datetime import datetime
from odoo.http import request, Response
from odoo import http

_logger = logging.getLogger(__name__)

class FormatResponse:

    def __init__(self, status_code, message, result=None):
        self.timestamp = datetime.utcnow().isoformat()
        self.status = status_code
        self.message = message
        self.result = result

    def to_dict(self):
        """Chuyển đổi phản hồi thành dictionary để chuyển đổi thành JSON"""
        return {
            'timestamp': self.timestamp,
            'status': self.status,
            'message': self.message,
            'result': self.result
        }

    def to_response(self):
        """Chuyển đổi phản hồi thành Response Odoo"""
        return Response(json.dumps(self.to_dict()), content_type='application/json', status=self.status)
