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

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline_does_nothing(self, mock_stdout):
        """Test that emptyline does nothing."""
        command = HBNBCommand()
        with patch('builtins.input', side_effect=['']):
            command.emptyline()
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline_with_nonempty_input(self, mock_stdout):
        """Test emptyline does nothing with non empty input."""
        command = HBNBCommand()
        with patch('builtins.input', side_effect=['some command']):
            command.emptyline()
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline_with_multiple_newlines(self, mock_stdout):
        """Test that emptyline does nothing with multiple newlines."""
        command = HBNBCommand()
        with patch('builtins.input', side_effect=['\n\n\n']):
            command.emptyline()
        self.assertEqual(mock_stdout.getvalue().strip(), "")


if __name__ == '__main__':
    unittest.main()
