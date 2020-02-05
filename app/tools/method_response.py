import logging

from flask import jsonify
from marshmallow import Schema, fields


logger = logging.getLogger(__name__)


class MethodResponse:
    def __init__(self, success=False, message=None, data=None):
        self.success = success
        self.message = message
        self.data = data
        if success and self.message:
            print(self.message)
        elif self.message:
            print(self.message)
            if self.data:
                print(f'Data: \n{self.data}')

    @classmethod
    def return_error(cls, message: str, data=None):
        return jsonify(
            MethodResponseSchema().dump(MethodResponse(message=message, data=data))), HttpStatus.BAD_REQUEST.value

    @classmethod
    def return_success(cls, message: str = None, data=None):
        return jsonify(
            MethodResponseSchema().dump(MethodResponse(success=True, message=message, data=data))), HttpStatus.OK.value

    def return_json(self):
        return jsonify(MethodResponseSchema().dump(self))


class MethodResponseSchema(Schema):
    success = fields.Bool()
    message = fields.Str()
    data = fields.Dict()
    version = fields.Str()