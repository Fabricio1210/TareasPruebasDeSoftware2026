import unittest
from unittest.mock import Mock
from PasswordValidation import passwordValidation

class TestPasswordValidation(unittest.TestCase):

    @patch('builtins.print')
    def test_password_too_short_message(self, mock_print):
        result = passwordValidation("123")
        self.assertFalse(result)
        mock_print.assert_called_once_with("Password must be at least 8 characters")

    @patch('builtins.print')
    def test_password_does_not_have_at_least_two_numbers(self, mock_print):
        result = passwordValidation("HolaComoEstas1")
        self.assertFalse(result)
        mock_print.assert_called_once_with("Password must contain at least 2 numbers")

    @patch('builtins.print')
    def test_password_valid_no_message(self, mock_print):
        result = passwordValidation("123456789")
        self.assertTrue(result)
        mock_print.assert_not_called()

    @patch('builtins.print')
    def test_multiple_errors(self, mock_print):
        """Caso clave: falla longitud Y falta de números simultáneamente."""
        resultado = passwordValidation("abc1")
        self.assertFalse(resultado)
        mensaje_esperado = "Password must be at least 8 characters\nThe password must contain at least 2 numbers"
        mock_print.assert_called_once_with(mensaje_esperado)