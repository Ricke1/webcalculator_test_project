import json
import os
import time

import pytest

from .req.base_request import BaseRequest


# Проверка на корректность формата запроса/ответа для API-методов и значения по умолчанию
def test_request_response_correctness():
    os.system('work_start\\webcalculator.exe stop')
    os.system('work_start\\webcalculator.exe start')

    # Проверка задачи state
    state = BaseRequest("state", "GET")
    assert state.make_request(), "Формат ответа не согласуется с описанием API-функции state"

    # Проверка задачи addition
    addition = BaseRequest("addition", "POST")
    assert addition.make_request(), "Формат ответа не согласуется с описанием API-функции addition"

    # Проверка задачи multiplication
    multiplication = BaseRequest("multiplication", "POST")
    assert multiplication.make_request(), "Формат ответа не согласуется с описанием API-функции multiplication"

    # Проверка задачи division
    division = BaseRequest("division", "POST")
    assert division.make_request(), "Формат ответа не согласуется с описанием API-функции division"

    # Проверка задачи remainder
    remainder = BaseRequest("remainder", "POST")
    assert remainder.make_request(), "Формат ответа не согласуется с описанием API-функции remainder"


# Проверка на правильность вычисления результата при указании допустимых входных данных
def test_calculations_correctness():
    args = {"x": -2147483648, "y": 2147483647}

    # Проверка задачи addition: сложение x и y
    addition = BaseRequest("addition", "POST")
    assert addition.make_request(args), "Результат вычисления webcalculator неверный"

    # Проверка задачи multiplication: умножение x и y
    multiplication = BaseRequest("multiplication", "POST")
    assert multiplication.make_request(args), "Результат вычисления webcalculator неверный"

    # Проверка задачи division: деление на цело x на y
    division = BaseRequest("division", "POST")
    assert division.make_request(args), "Результат вычисления webcalculator неверный"

    # Проверка задачи remainder: остаток от деления x на y
    remainder = BaseRequest("remainder", "POST")
    assert remainder.make_request(args), "Результат вычисления webcalculator неверный"


# Проверка: Работает ли калькулятор после его выключения через консоль?
def test_webcalculator_on_or_off():
    print("Выключение калькулятора")

    # Остановка калькулятора
    os.system('work_start\\webcalculator.exe stop')

    # Тестовый запрос, который проверяет наличие ошибки ConnectionError
    state = BaseRequest("state", "GET")
    assert state.check_application_management_functionality(test_mode=1)
    print("Вебкалькулятор успешно выключен, запрос не отправлен ")

# Проверка возможности смены адреса хоста/порта
def test_webcalculator_change_host_or_port_address():
    IP = 'localhost'
    PORT = '5413'

    os.system(f'work_start\\webcalculator.exe start {IP} {PORT}')

    # Тестовый запрос, в котором имя задачи и тип запроса изменены на новый адрес и порт, так как имя задачи
    # и тип запроса предопределены заранее
    state = BaseRequest(IP, PORT)
    assert state.check_application_management_functionality(test_mode=2),  "Получен неверный ответ от сервера"

    os.system('work_start\\webcalculator.exe stop')
