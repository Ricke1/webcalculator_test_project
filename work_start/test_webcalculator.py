import os

import pytest

from .req.base_request import BaseRequest


# Проверка на корректность формата запроса/ответа для API-методов и значения по умолчанию
def test_request_response_correctness():
    print('\nТест на корректность формата запроса/ответа'.upper())

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

    print('Тест #1 выполнен успешно'.upper())


# Проверка на правильность вычисления результата при указании допустимых входных данных
def test_calculations_correctness():
    print('\nТест на правильность вычисления результата'.upper())
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

    print('Тест #2 выполнен успешно'.upper())


# Проверка: Работает ли калькулятор после его выключения через консоль?
def test_webcalculator_on_or_off():
    print("\nТест провяющий функционал выключения калькулятора".upper())

    # Остановка калькулятора
    os.system('work_start\\webcalculator.exe stop')

    # Тестовый запрос, который проверяет наличие ошибки ConnectionError
    state = BaseRequest("state", "GET")
    assert state.check_application_management_functionality(test_case=1)

    print('Тест #3.1 выполнен успешно'.upper())


# Проверка возможности смены адреса хоста/порта
def test_webcalculator_change_host_and_port_address_and_possibility_of_restart():
    print('\nТест проверяющий возможность смееы адреса хоста/порта'.upper())
    IP = 'localhost'
    PORT = '5413'

    os.system(f'work_start\\webcalculator.exe start {IP} {PORT}')

    # Тестовый запрос, в котором имя задачи и тип запроса изменены на новый адрес и порт, так как имя задачи
    # и тип запроса предопределены заранее
    state = BaseRequest(IP, PORT)
    assert state.check_application_management_functionality(test_case=2), "Получен неверный ответ от сервера"

    os.system('work_start\\webcalculator.exe restart')
    assert state.check_application_management_functionality(test_case=3), "После рестарта изменился адрес или порт"

    os.system('work_start\\webcalculator.exe stop')

    print('Тест #3.2 выполнен успешно'.upper())


# Тест проверяющий правильность возвращения кода ошибки 1
def test_error_code_1():
    print("\nТест проверяющий правильность возвращения кода ошибки 1".upper())
    os.system('work_start\\webcalculator.exe start')

    error_code = BaseRequest.correct_error_answer_form()
    assert error_code == 1, f'Ожидается код ошибки: 1. Получен код ошибки: {error_code}'

    print('Тест #4.1 выполнен успешно'.upper())


# Тест проверяющий правильность возвращения кода ошибки 2
def test_error_code_2():
    print("\nТест проверяющий правильность возвращения кода ошибки 2".upper())

    # Изменение кода ошибки получаем с помощью изменения передаваемых аргументов
    args = {"x": 100}
    error_code = BaseRequest.correct_error_answer_form(args)
    assert error_code == 2, f'Ожидается код ошибки: 2. Получен код ошибки: {error_code}'

    print('Тест #4.2 выполнен успешно'.upper())


# Тест проверяющий правильность возвращения кода ошибки 3

def test_error_code_3():
    print("\nТест проверяющий правильность возвращения кода ошибки 3".upper())

    args = {'x': 100, 'y': 100.50}
    error_code = BaseRequest.correct_error_answer_form(args)
    assert error_code == 3, f'Ожидается код ошибки: 3. Получен код ошибки: {error_code}'

    print('Тест #4.3 выполнен успешно'.upper())


# Тест проверяющий правильность возвращения кода ошибки 4

def test_error_code_4():
    print("\nТест проверяющий правильность возвращения кода ошибки 4".upper())

    args = {'x': 3147483647, 'y': 100}
    error_code = BaseRequest.correct_error_answer_form(args)
    assert error_code == 4, f'Ожидается код ошибки: 4. Получен код ошибки: {error_code}'

    print('Тест #4.4 выполнен успешно'.upper())


# Тест проверяющий правильность возвращения кода ошибки 5

def test_error_code_5():
    print("\nТест проверяющий правильность возвращения кода ошибки 5".upper())

    args = {"x": 0,"y":0}
    error_code = BaseRequest.correct_error_answer_form(args)
    assert error_code == 5, f'Ожидается код ошибки: 5. Получен код ошибки: {error_code}'

    print('Тест #4.5 выполнен успешно'.upper())
    os.system('work_start\\webcalculator.exe stop')
