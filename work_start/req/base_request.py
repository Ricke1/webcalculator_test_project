from .locators import ApiLocators
import requests


class BaseRequest:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def make_request(self, args=None):
        if args is None:
            args = {"x": 1, "y": 1}

        if self.name == "state" and self.type == "GET":
            try:
                r = requests.get(ApiLocators.STATE_API_URL)
            except requests.exceptions.ConnectionError:
                assert False, "Не удалось установить соединение, возможно приложение не запущено"
            info = r.json()
            if info['statusCode'] == 0 and "OК" in info['state']:
                return True

        elif self.name == "addition" and self.type == "POST":
            try:
                r = requests.post(ApiLocators.ADDITION_API_URL, json=args)
            except requests.exceptions.ConnectionError:
                assert False, "Не удалось установить соединение, возможно приложение не запущено"
            info = r.json()
            if info['statusCode'] == 0 and info['result'] == (args['x']+args['y']):
                return True
        else:
            assert False, "Неправильный формат запроса"
