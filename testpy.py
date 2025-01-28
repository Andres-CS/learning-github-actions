import pytest
def return_hello():
    return "hello"

def test_return_hello():
    assert return_hello() == "hello"