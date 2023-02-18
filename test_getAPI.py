import pytest as pytest

from grocery import *
import requests


except_status = 200
except_text = '{"status":"UP"}'
except_content = b'{"status":"UP"}'
except_json = {'status': 'UP'}

def test_get_status():
    resp = requests.get(STATUS_ENDPOINT)
    print(resp.text)
    assert except_text == resp.text
    print(resp.status_code)
    assert except_status == resp.status_code
    print(resp.content)
    assert except_content == resp.content
    print(resp.json())
    assert except_json == resp.json()

test_get_status()








