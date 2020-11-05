from flask import make_response

def bad_request(error):
    return make_response({ 'status': 'bad request' }, 400)

def unhandled_exception(exception):
    return make_response({ 'status': 'unhandled_exception' }, 500)