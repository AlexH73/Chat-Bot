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
        with self.assertRaises(SystemExit):  # expect exit
           choose_language(LANGUAGES)  # if input is not 1, 2 or 3, it should exit


class TestChooseItem(unittest.TestCase):

    def setUp(self):
        self.lang = LANGUAGES["en"]  # задаем язык для тестов

    @patch('builtins.input', return_value="1")
    def test_choose_first_item(self, mock_input):
        """Тест на выбор первого блюда"""
        category_name = "main_course"
        items = CATEGORIES[category_name]["items"]
        expected_item = items[0]
        actual_item = choose_item(items, category_name, self.lang, "en", show_back=True)
        self.assertEqual(actual_item["name"], expected_item["name"]["en"])
        self.assertEqual(actual_item["price"], expected_item["price"])

    @patch('builtins.input', side_effect=["9"])
    def test_choose_back(self, mock_input):
        """Тест на выбор опции назад"""
        category_name = "main_course"
        items = CATEGORIES[category_name]["items"]
        actual_item = choose_item(items, category_name, self.lang, "en", show_back=True)
        self.assertEqual(actual_item, "back")

    @patch('builtins.input', side_effect=["a", "9"])
    def test_choose_invalid_item(self, mock_input):
        """Тест на выбор некорректного блюда"""
        category_name = "main_course"
        items = CATEGORIES[category_name]["items"]
        actual_item = choose_item(items, category_name, self.lang, "en", show_back=True)
        self.assertEqual(actual_item, "back")


if __name__ == '__main__':
    unittest.main()
