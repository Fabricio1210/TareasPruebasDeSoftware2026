import unittest
from unittest.mock import Mock
from PasswordValidation import passwordValidation

class TestPasswordValidation(unittest.TestCase):

    @patch('builtins.print')
    def test_password_too_short_message(self, mock_print):
        result = passwordValidation("H123")
        self.assertFalse(result)
        mock_print.assert_called_once_with("Password must be at least 8 characters")

    @patch('builtins.print')
    def test_password_does_not_have_at_least_two_numbers(self, mock_print):
        result = passwordValidation("HolaComoEstas1")
        self.assertFalse(result)
        mock_print.assert_called_once_with("Password must contain at least 2 numbers")

    @patch('builtins.print')
    def test_password_valid_no_message(self, mock_print):
        result = passwordValidation("Hola123456789!")
        self.assertTrue(result)
        mock_print.assert_not_called()

    @patch('builtins.print')
    def test_missing_capital_only(self, mock_print):
        self.assertFalse(passwordValidation("clave123jola"))
        mock_print.assert_called_once_with("password must contain at least one capital letter")

    @patch('builtins.print')
    def test_missing_special_only(self, mock_print):
        self.assertFalse(passwordValidation("Password12"))
        mock_print.assert_called_once_with("password must contain at least one special character")

    @patch('builtins.print')
    def test_multiple_errors(self, mock_print):
        self.assertFalse(passwordValidation("abc1"))      
        mensaje_esperado = (
            "Password must be at least 8 characters\n"
            "The password must contain at least 2 numbers\n"
            "password must contain at least one capital letter\n"
            "password must contain at least one special character"
        )
        mock_print.assert_called_once_with(mensaje_esperado)