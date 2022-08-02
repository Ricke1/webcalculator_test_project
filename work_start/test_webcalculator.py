import json
from .req.base_request import BaseRequest


def test_request_response_correctness():
    state = BaseRequest("state", "GET")
    assert state.make_request(), "Формат ответа не согласуется с описанием API-функции state"

    addition = BaseRequest("addition", "POST")
    assert  addition.make_request(), "Формат ответа не согласуется с описанием API-функции addition"
