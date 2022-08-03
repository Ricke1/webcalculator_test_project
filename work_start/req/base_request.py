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
                print(args['x'] * args['y'])
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

    def check_application_management_functionality(self, test_mode=1):
        # Если test_mode = 1, то происходит проверка: Выключился ли калькулятор?
        if test_mode == 1:
            try:
                requests.get(ApiLocators.STATE_API_URL)
            except requests.exceptions.ConnectionError:
                return True
        # Если test_mode = 1, то происходит проверка:
        elif test_mode == 2:
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
