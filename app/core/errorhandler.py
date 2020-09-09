from werkzeug.exceptions import BadRequest
from marshmallow import ValidationError as MarshmallowError
from requests import RequestException
from flask_restplus import abort
import re


class ErrorHandler(object):
    """ Main error handler of application

    Attributes
    ----------
    error: Captured error

    Methods
    -------
    handle()
        Identify and generate status code and message for errors
    """

    def __init__(self, error):
        self.__error = error

    def handle(self):
        errors = {
            MarshmallowError: self._handleMarshmallowError,
            RequestException: self._handleRequestException,
            BadRequest: self._handleBadRequestException,
        }
        for errType, errHandler in errors.items():
            if isinstance(self.__error, errType):
                return errHandler()
        return self._defaultHandler()

    @property
    def error(self):
        return self.__error

    def _handleRequestException(self):
        abort(400, error=str(self.error))

    def _handleBadRequestException(self):
        abort(422, error=str(self.error))

    def _handleMarshmallowError(self):
        message = re.sub(r'[\{\[\}\]\'}]', "", self.error.messages.__str__())
        abort(422, error=message)

    def _defaultHandler(self):
        abort(500, error="Ocorreu um erro interno no servidor.")



