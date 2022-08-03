import json
import os
import time

from .req.base_request import BaseRequest


def test_request_response_correctness():
    os.system('work_start\webcalculator.exe start')

    state = BaseRequest("state", "GET")
    assert state.make_request(), "Формат ответа не согласуется с описанием API-функции state"

    addition = BaseRequest("addition", "POST")
    assert addition.make_request(), "Формат ответа не согласуется с описанием API-функции addition"

    multiplication = BaseRequest("multiplication", "POST")
    assert multiplication.make_request(), "Формат ответа не согласуется с описанием API-функции multiplication"

    division = BaseRequest("division", "POST")
    assert division.make_request(), "Формат ответа не согласуется с описанием API-функции division"

    remainder = BaseRequest("remainder", "POST")
    assert remainder.make_request(), "Формат ответа не согласуется с описанием API-функции remainder"


def test_calculations_correctness():
    args = {"x": -2147483648, "y": 2147483647}

    addition = BaseRequest("addition", "POST")
    assert addition.make_request(args), "Результат вычисления webcalculator неверный"

    multiplication = BaseRequest("multiplication", "POST")
    assert multiplication.make_request(args), "Результат вычисления webcalculator неверный"

    division = BaseRequest("division", "POST")
    assert division.make_request(args), "Результат вычисления webcalculator неверный"

    remainder = BaseRequest("remainder", "POST")
    assert remainder.make_request(args), "Результат вычисления webcalculator неверный"


def test_webcalculator():

    os.system('work_start\webcalculator.exe stop')

    state = BaseRequest("state", "GET")
    assert state.check_application_management_functionality(test_mode=1)
