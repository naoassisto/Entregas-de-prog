
import unittest
from unittest.mock import patch
from src.conversao import celsius_para_fahrenheit

class TestConversaoComMock(unittest.TestCase):
    @patch('src.conversao.obter_temperatura_celsius')
    def test_celsius_para_fahrenheit(self, mock_obter_temperatura):
        mock_obter_temperatura.return_value = 0
        self.assertEqual(celsius_para_fahrenheit(mock_obter_temperatura()), 32)

if __name__ == '__main__':
    unittest.main()
