# -*- coding: utf-8 -*-

import pytest
from flexx_project.skeleton import fib

__author__ = "PryderiNudd"
__copyright__ = "PryderiNudd"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
