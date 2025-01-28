import unittest
import os
from ui import choose_language, choose_item
from unittest.mock import patch
from data import LANGUAGES, CATEGORIES


class TestChooseLanguage(unittest.TestCase):

    @patch('builtins.input', side_effect=["1"])
    def test_choose_english(self, mock_input):
        """Тест на выбор английского языка"""
        self.assertEqual(choose_language(LANGUAGES), "en")

    @patch('builtins.input', side_effect=["2"])
    def test_choose_russian(self, mock_input):
        """Тест на выбор русского языка"""
        self.assertEqual(choose_language(LANGUAGES), "ru")

    @patch('builtins.input', side_effect=["3"])
    def test_choose_german(self, mock_input):
        """Тест на выбор немецкого языка"""
        self.assertEqual(choose_language(LANGUAGES), "de")

    @patch('builtins.input', side_effect=["4", "1"])
    def test_choose_invalid_language(self, mock_input):
        """Тест на некорректный ввод языка"""
        with self.assertRaises(SystemExit) as context:
           choose_language(LANGUAGES)
        self.assertEqual(context.exception.code, 1)


class TestChooseItem(unittest.TestCase):
    @patch('builtins.input', side_effect=["1", "0"])
    @patch('builtins.print')
    def test_choose_item_pizza(self, mock_print, mock_input):
        """Тест на выбор пиццы без добавок"""
        self.assertEqual(choose_item(LANGUAGES["en"], "main"), 1)
        mock_print.assert_called_with("Added: Pizza")

    @patch('builtins.input', side_effect=["2", "1", "0"])
    @patch('builtins.print')
    def test_choose_item_pasta_with_cheese(self, mock_print, mock_input):
        """Тест на выбор пасты c сыром"""
        self.assertEqual(choose_item(LANGUAGES["en"], "main"), 2)
        mock_print.assert_called_with("Added: Pasta")
        mock_print.assert_called_with("Added: Cheese")

    @patch('builtins.input', side_effect=["5", "1", "0"])
    @patch('builtins.print')
    def test_choose_item_invalid_choice(self, mock_print, mock_input):
        """Тест на некорректный ввод"""
        self.assertEqual(choose_item(LANGUAGES["en"], "main"), None)
        mock_print.assert_called_with("Invalid choice. Please try again.")

    @patch('builtins.input', side_effect=["9"])
    @patch('builtins.print')
    def test_choose_item_go_back(self, mock_print, mock_input):
      """Тест на возврат в предыдущее меню"""
      self.assertEqual(choose_item(LANGUAGES["en"], "main"), 9)
      mock_print.assert_not_called()


if __name__ == '__main__':
    unittest.main()
