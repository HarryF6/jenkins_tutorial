# python/test_dummy.py

from . import hello_world


def test_dummy():
    assert True

def test_hello():
    hello_world.hello()
