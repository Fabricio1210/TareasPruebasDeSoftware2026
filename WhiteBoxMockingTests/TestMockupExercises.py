# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import unittest
from unittest.mock import patch, mock_open
import subprocess
from MockupExercises import fetch_data_from_api, perform_action_based_on_time, read_data_from_file, execute_command


class TestFetchDataFromApi(unittest.TestCase):
    """
    Fetch data from API unittest class.
    """

    @patch("MockupExercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Success case.
        """
        mock_get.return_value.json.return_value = [
            {"id": 1, "article": "Laptop HP", "price": "20000"},
            {"id": 2, "article": "Galletas Oreo", "price": "67"},
            {"id": 3, "article": "Bicicleta", "price": "12500"},
            {"id": 4, "article": "Jamon", "price": "50"},
        ]
        mock_get.return_value.status_code = 200
        result = fetch_data_from_api("https://api.example.com/data")
        self.assertEqual(result, [
            {"id": 1, "article": "Laptop HP", "price": "20000"},
            {"id": 2, "article": "Galletas Oreo", "price": "67"},
            {"id": 3, "article": "Bicicleta", "price": "12500"},
            {"id": 4, "article": "Jamon", "price": "50"},
        ])
        self.assertEqual(mock_get.return_value.status_code, 200)
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)


class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Perform Action Based On Time unittest class.
    """

    @patch("MockupExercises.time.time")
    def test_perform_action_based_on_time_action_a(self, mock_time):
        """
        Action A.
        """
        mock_time.return_value = 5
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")

    @patch("MockupExercises.time.time")
    def test_perform_action_based_on_time_action_b(self, mock_time):
        """
        Action B.
        """
        mock_time.return_value = 15
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")

class TestReadDataFromFile(unittest.TestCase):
    """
    Open the file to read the content
    """

    @patch("builtins.open", new_callable=mock_open, read_data="Hola mundo")
    def test_read_data_from_file_success(self,mock_file):
        result = read_data_from_file("Hola.txt")
        self.assertEqual(result,"Hola mundo")
        mock_file.assert_called_once_with("Hola.txt", encoding="utf-8")

    @patch("builtins.open")
    def test_read_data_from_no_existing_file(self,mock_open):
        mock_open.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("archivo.txt")

class TestExecuteCommand(unittest.TestCase):
    """
    Execute a command using subproceses
    """

    @patch("MockupExercises.subprocess.run")
    def execute_command(self, mock_run):
        mock_run.return_value.stdout = "Se sobrevivio al ejercicio"
        result = execute_command(["echo", "Hola mundo"])
        self.assertEqual(result, "Se sobrevivio al ejercicio")
        mock_run.assert_called_once_with(
            ["echo", "Hola mundo"],
            capture_output=True,
            check=False,
            text=True
        )

    @patch("MockupExercises.subprocess.run")
    def test_execute_command_error(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(1, "cmd")
        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["cmd"])

if __name__ == '__main__':
    unittest.main()