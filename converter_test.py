import pytest
from hexorcist import to_decimal, from_decimal

import unittest

"""Tests binary to all bases"""

def test_binary_to_octal():
    """Tests to see if a binary value equals the right octal value."""
    decimal_value = to_decimal("1010", 2)
    octal_value = from_decimal(decimal_value, 8)
    assert octal_value == "12"

def test_binary_to_decimal():
    """Tests to see if a binary value equals the right decimal value."""
    assert to_decimal("1010", 2) == 10

def test_binary_to_hex():
    """Tests to see if a binary value equals the right hex value."""
    decimal_value = to_decimal("1010", 2)
    hex_value = from_decimal(decimal_value, 16)
    assert hex_value == "A"

def test_binary_to_binary():
    """Tests to see if a binary value equals the right binary value (itself)."""
    decimal_value = to_decimal("1010", 2) 
    result = from_decimal(decimal_value, 2)
    assert result == "1010"

"""Tests octal to all bases"""
def test_octal_to_binary():
    """Tests to see if a octal value equals the right binary value."""
    decimal_value = to_decimal("12", 8)
    binary_value = from_decimal(decimal_value, 2)
    assert binary_value == "1010"

def test_octal_to_decimal():
    """Tests to see if a octal value equals the right decimal value."""
    assert to_decimal("12", 8) == 10

def test_octal_to_hex():
    """Tests to see if a octal value equals the right hex value."""
    decimal_value = to_decimal("12", 8)
    hex_value = from_decimal(decimal_value, 16)
    assert hex_value == "A"

def test_octal_to_octal():
    """Tests to see if a octal value equals the right octal value (itself)."""
    decimal_value = to_decimal("12", 8) 
    result = from_decimal(decimal_value, 8)
    assert result == "12"


"""Tests decimal to all bases"""
def test_decimal_to_binary():
    """Tests to see if a decimal value equals the right binary value."""
    assert from_decimal(10, 2) == "1010"

def test_decimal_to_octal():
    """Tests to see if a decimal value equals the right octal value."""
    assert from_decimal(10, 8) == "12"

def test_decimal_to_hex():
    """Tests to see if a decimal value equals the right hex value."""
    assert from_decimal(199, 16) == "C7"

def test_decimal_to_decimal():
    """Tests to see if a decimal value equals the right decimal value (itself)."""
    assert from_decimal(10, 10) == "10"
 

"""Tests hex to all bases"""
def test_hex_to_binary():
    """Tests to see if a hex value equals the right binary value."""
    decimal_value = to_decimal("C7", 16)
    binary_value = from_decimal(decimal_value, 2)
    assert binary_value == "11000111"

def test_hex_to_decimal():
    """Tests to see if a hex value equals the right decimal value."""
    assert to_decimal("C7", 16) == 199

def test_hex_to_octal():
    """Tests to see if a hex value equals the right octal value."""
    decimal_value = to_decimal("C7", 16)
    octal_value = from_decimal(decimal_value, 8)
    assert octal_value == "307"

def test_hex_to_hex():
    """Tests to see if a hex value equals the right hex  (itself)."""
    decimal_value = to_decimal("C7", 16) 
    result = from_decimal(decimal_value, 16)
    assert result == "C7"


"""Tests incase zero is the initial/current base conversion, is so, 0 will be returned"""
def test_for_zero():
    assert from_decimal(0, 8) == "0"
    assert to_decimal("0", 16) == 0

