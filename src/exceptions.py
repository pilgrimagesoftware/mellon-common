__author__ = "Paul Schifferer <paul@schifferers.net>"

from app import app
from flask import jsonify


class ApprovalException(Exception):
    message = ""

    def __init__(self, message):
        super().__init__()
        self.message = message


class APIException(Exception):
    status_code = None

    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        return rv


class InvalidAppIDException(APIException):
    status_code = 400
    message = "The request did not an app ID or the app ID was incorrect."


class SignatureMissingException(APIException):
    status_code = 400
    message = "The request did not contain the expected signature header."


class InvalidSignatureException(APIException):
    status_code = 403
    message = "The request signature did not match."


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
