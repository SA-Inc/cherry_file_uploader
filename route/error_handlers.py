from flask import Blueprint
import controller.error_handlers

error_handlers = Blueprint('error_handlers', __name__)

@error_handlers.errorhandler(400)
def bad_request(error):
    return controller.error_handlers.bad_request(error)

# def server_error(error):
#     return controller.error_handlers.server_error(error)

@error_handlers.errorhandler(Exception)
def unhandled_exception(exception):
    return controller.error_handlers.unhandled_exception(exception)