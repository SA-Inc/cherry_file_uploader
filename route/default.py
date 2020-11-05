# модуль для HTML шаблонов
from flask import Blueprint
# импорт обработчиков
import controller.default

# регистрация шаблона
default = Blueprint('default', __name__)

# непосредственно сами обработчики HTTP. 1 для страницы с формой, 2 для обработка CSV файла
@default.route('/', methods = ['GET'])
def home():
    return controller.default.home()

@default.route('/form_file', methods = ['POST'])
def form_file():
    return controller.default.form_file()