from flask_httpauth import HTTPBasicAuth
from app.models import User
from app.api.errors import error_response
from flask_httpauth import HTTPTokenAuth

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
@token_auth.verify_token
def verify_password(token):
    return User.check_token(token) if token else None

@basic_auth.error_handler
def basic_auth_error(status):
    return error_response(status)
