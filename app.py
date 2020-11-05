from flask import Flask, make_response
from flask_cors import CORS

# создание сервачка и определение, где брать HTML файлы. А так же разрешение CORS
app = Flask(__name__, template_folder = 'view', static_folder = 'view')
CORS(app, resources = { r"/*": { "origins": "*" } })

# Импорт HTTP маршрутов
from route.default import default
from route.error_handlers import error_handlers


# ответ на классические ошибки HTTP
@app.errorhandler(404)
def not_found(error):
    return make_response({ 'status': 'not found' }, 404)

@app.errorhandler(405)
def method_not_found(error):
    return make_response({ 'status': 'method not allowed' }, 405)

@app.errorhandler(500)
def server_error(error):
    return make_response({ 'status': 'internal server error', 'error': error }, 500)


# регистрация маршрутов
app.register_blueprint(error_handlers)
app.register_blueprint(default, url_prefix = '/')


# Запуск сервачка
if __name__ == '__main__':
    app.run(debug = True)