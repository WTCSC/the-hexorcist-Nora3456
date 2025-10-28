import pytest

from converter_test import decimal_to_binary, decimal_to_octal, decimal_to_hex


"""Test 0 as an option for input to hex"""
def test_binary_hex_0():
    assert decimal_to_binary(0) == 0
