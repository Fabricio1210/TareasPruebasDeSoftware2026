import pytest
from point_of_sale import App

app = App()

def test_given12345_returns725():
    assert app.scan("12345") == "$7.25"

def test_given23456_returns1250():
    assert app.scan("23456") == "$12.50"

def test_given9999_returnserror():
    assert app.scan("99999") == "Error: barcode not found"

def test_givenemptystr_returnserror():
    assert app.scan("") == "Error: empty barcode"

