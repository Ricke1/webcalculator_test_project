from .locators import ApiLocators
import requests


class BaseRequest:

    def __init__(self, name, typeof):
        self.name = name
        self.typeof = typeof

    def make_request(self, args=None):
        if args is None:
            args = {"x": 1, "y": 1}

        if self.name == "state" and self.typeof == "GET":
            try:
                r = requests.get(ApiLocators.STATE_API_URL)
            except requests.exceptions.ConnectionError:
                assert False, "Не удалось установить соединение, возможно приложение не запущено"
            info = r.json()
            if info['statusCode'] == 0 and "OК" in info['state']:
                return True
            else:
                return False

        elif self.name == "addition" and self.typeof == "POST":
            try:
                r = requests.post(ApiLocators.ADDITION_API_URL, json=args)
            except requests.exceptions.ConnectionError:
                assert False, "Не удалось установить соединение, возможно приложение не запущено"
            info = r.json()
            if info['statusCode'] == 0 and info['result'] == (args['x'] + args['y']):
                return True
            else:
                return False

        elif self.name == "multiplication" and self.typeof == "POST":
            try:
                r = requests.post(ApiLocators.MULTIPLICATION_API_URL, json=args)
            except requests.exceptions.ConnectionError:
                assert False, "Не удалось установить соединение, возможно приложение не запущено"
            info = r.json()
            if info['statusCode'] == 0 and info['result'] == (args['x'] * args['y']):
                return True
            else:
                return False

        elif self.name == "division" and self.typeof == "POST":
            try:
                r = requests.post(ApiLocators.DIVISION_API_URL, json=args)
            except requests.exceptions.ConnectionError:
                assert False, "Не удалось установить соединение, возможно приложение не запущено"
            info = r.json()
            if info['statusCode'] == 0 and info['result'] == (args['x'] // args['y']):
                return True
            else:
                return False

        elif self.name == "remainder" and self.typeof == "POST":
            try:
                r = requests.post(ApiLocators.REMAINDER_API_URL, json=args)
            except requests.exceptions.ConnectionError:
                assert False, "Не удалось установить соединение, возможно приложение не запущено"
            info = r.json()
            if info['statusCode'] == 0 and info['result'] == (args['x'] % args['y']):
                return True
            else:
                return False

        else:
            assert False, "Неправильный формат запроса"

    def check_application_management_functionality(self, test_case=1):
        # Если test_mode = 1, то происходит проверка: Выключился ли калькулятор?
        if test_case == 1:
            try:
                requests.get(ApiLocators.STATE_API_URL)
            except requests.exceptions.ConnectionError:
                return True
        # Если test_mode = 2, то происходит проверка отправки запроса на сервер с другим адресом хоста и порта
        elif test_case == 2:
            try:
                r = requests.get(f"http://{self.name}:{self.typeof}/api/state")
                print("Соединение установлено успешно")
            except requests.exceptions.ConnectionError:
                assert False, "Не удалось установить соединение, возможно приложение не запущено или указан неверный " \
                              "адресс "
            info = r.json()
            if info['statusCode'] == 0 and "OК" in info['state']:
                return True
            else:
                return False
        # Если test_mode = 3, то проиходит проверка возможности рестарта вебкалькулятора с сохранением адреса и порта
        elif test_case == 3:
            try:
                requests.get(f"http://{self.name}:{self.typeof}/api/state")
                print("После перезапуска соединение установлено успешно")
                return True
            except requests.exceptions.ConnectionError:
                assert False, "Не удалось установить соединение, возможно приложение не запущено или указан неверный " \
                              "адресс "

    # Проверка на правильность возвращаемых ошибок
    @staticmethod
    def correct_error_answer_form(test_case=1):
        # В данном сценарии рассматривается код ошибки 1
        if test_case == 1:
            args = {"x": 100, "y": 0}
            try:
                r = requests.post(ApiLocators.DIVISION_API_URL, json=args)
                info = r.json()
                print("info[statusCode] =", info['statusCode'])
                if info['statusCode'] == 1:
                    return True
            except requests.exceptions.ConnectionError:
                assert False, "Не удалось установить соединение, возможно приложение не запущено"
