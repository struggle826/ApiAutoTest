'''
fixture 带返回值
'''
import pytest
@pytest.fixture()
def data():
    return{"username":"root","pwd":"123456"}

def test_case01(data):
    print("{data}")
    print("{data['username']}")
    print("{data['pwd']}")