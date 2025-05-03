import unittest
from unittest.mock import patch
from calculate.view import View

class TestView(unittest.TestCase):
    @patch("builtins.input", return_value="mocked")
    def test_get_user_input(self, mock_input):
        self.assertEqual(View.get_user_input("msg"), "mocked")