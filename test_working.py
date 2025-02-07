import pytest
import sys
from working import convert

def test_convert0():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def test_convert1():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'

def test_convert2():
    assert convert('10 AM to 8:50 PM') == '10:00 to 20:50'

def test_convert3():
    assert convert('10:30 PM to 8 AM') == '22:30 to 08:00'

def test_convert4():
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'

# Tests for invalid input (expecting ValueError)
def test_ve():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')

def test_ve1():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')

def test_ve2():
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')
