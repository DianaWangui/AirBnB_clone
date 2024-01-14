#!/usr/bin/python3
"""Module to test the console and its function."""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommandsMethods(unittest.TestCase):
    """Creating test cases for the console."""
    @patch('builtins.input', side_effect=['quit'])
    def test_do_quit(self, mock_input):
        """Test the inbuilt method do_quit method."""
        command = HBNBCommand()
        result = command.onecmd('quit')
        self.assertTrue(result)

    @patch('builtins.input', side_effect=[''])
    def test_do_EOF(self, mock_input):
        """Test the inbuilt method EOF."""
        command = HBNBCommand()
        result = command.onecmd('quit')
        self.assertTrue(result)

    def test_help_quit(self):
        """Test the inbuilt method help_quit."""
        command = HBNBCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            command.do_help('quit')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Quit command to exit the program")


if __name__ == '__main__':
    unittest.main()
