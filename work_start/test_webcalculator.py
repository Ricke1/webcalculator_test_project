import json
from .req.base_request import BaseRequest


def test_request_response_correctness():
    state = BaseRequest("STATE", "GET")
    assert state.make_request()
