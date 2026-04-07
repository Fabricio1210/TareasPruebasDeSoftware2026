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
    def test_password_valid_no_message(self, mock_print):
        result = passwordValidation("123456789")
        self.assertTrue(result)
        mock_print.assert_not_called()