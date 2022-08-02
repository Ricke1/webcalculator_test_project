from .locators import ApiLocators
import requests


class BaseRequest:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def make_request(self, args=None):
        if args is None:
            args = {"x": 1, "y": 1}

        if self.name == "STATE" and self.type == "GET":
            r = requests.get(ApiLocators.STATE_API_URL)
            print(r.json())

        elif self.name == "ADDITION" and self.type == "POST":
            r = requests.get(ApiLocators.ADDITION_API_URL, json=args)
            return
