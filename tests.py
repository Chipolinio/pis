import unittest
from unittest.mock import mock_open, patch
from io import StringIO

from Parser import Parser
from errors import ParsingError, ValidationError
from CurrencyRate import CurrencyRate
from HistoricalRate import HistoricalRate
from RateWithSource import RateWithSource
from RateWithFee import RateWithFee


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_parse_currency_rate_valid(self):
        input_str = '"USD" "RUB" 98.50 2025.09.03'
        obj = self.parser.parse_currency_rate(input_str)
        self.assertIsInstance(obj, CurrencyRate)
        self.assertEqual(obj.from_currency, "USD")
        self.assertEqual(obj.to_currency, "RUB")
        self.assertEqual(obj.rate, 98.50)
        self.assertEqual(obj.date, ('2025', '09', '03'))
        self.assertIn(obj, self.parser.currency_rate)

    def test_parse_currency_rate_invalid(self):
        with self.assertRaises(ParsingError):
            self.parser.parse_currency_rate('"USD" "RUB" abc 2025.09.03')
        with self.assertRaises(ParsingError):
            self.parser.parse_currency_rate('"USD" "RUB" 98.50 2025-09-03')

    def test_parse_historical_rate_valid(self):
        input_str = '"USD" "RUB" 88.50 2025.09.01 2025.09.03'
        obj = self.parser.parse_historical_rate(input_str)
        self.assertIsInstance(obj, HistoricalRate)
        self.assertEqual(obj.from_date, ('2025', '09', '01'))
        self.assertEqual(obj.to_date, ('2025', '09', '03'))
        self.assertIn(obj, self.parser.historical_rate)

    def test_parse_historical_rate_invalid(self):
        with self.assertRaises(ParsingError):
            self.parser.parse_historical_rate('"USD" "RUB" 88.50 2025.09.01')
        with self.assertRaises(ParsingError):
            self.parser.parse_historical_rate('"USD" "RUB" 88.50 2025.09.01 2025-09-03')

    def test_parse_rate_with_source_valid(self):
        input_str = '"USD" "RUB" 88.50 2025.09.03 "Сбер"'
        obj = self.parser.parse_rate_with_source(input_str)
        self.assertIsInstance(obj, RateWithSource)
        self.assertEqual(obj.source, "Сбер")
        self.assertIn(obj, self.parser.rate_with_source)

    def test_parse_rate_with_source_invalid(self):
        with self.assertRaises(ParsingError):
            self.parser.parse_rate_with_source('"USD" "RUB" 88.50 2025.09.03 ""')

    def test_parse_rate_with_fee_valid(self):
        input_str = '"USD" "RUB" 88.50 2025.09.03 0.5'
        obj = self.parser.parse_rate_with_fee(input_str)
        self.assertIsInstance(obj, RateWithFee)
        self.assertEqual(obj.fee, 0.5)
        self.assertIn(obj, self.parser.rate_with_fee)

    def test_parse_rate_with_fee_invalid(self):
        with self.assertRaises(ParsingError):
            self.parser.parse_rate_with_fee('"USD" "RUB" 88.50 2025.09.03 -0.5')

    def test_validation_negative_rate(self):
        with self.assertRaises(ValidationError):
            CurrencyRate(from_currency="USD", to_currency="RUB", rate=-10, date=("2025", "09", "03"))

    def test_validation_negative_fee(self):
        with self.assertRaises(ValidationError):
            RateWithFee(from_currency="USD", to_currency="RUB", rate=98.5, date=("2025", "09", "03"), fee=-0.5)

    def test_get_all_value(self):
        self.parser.parse_currency_rate('"USD" "RUB" 98.50 2025.09.03')
        self.parser.parse_historical_rate('"EUR" "RUB" 98.50 2025.08.01 2025.09.01')
        all_values = self.parser.get_all_value()
        self.assertEqual(len(all_values), 2)
        self.assertTrue(any(isinstance(v, CurrencyRate) for v in all_values))
        self.assertTrue(any(isinstance(v, HistoricalRate) for v in all_values))

    def test_clear_data(self):
        self.parser.parse_currency_rate('"USD" "RUB" 98.50 2025.09.03')
        self.parser.parse_historical_rate('"EUR" "RUB" 98.50 2025.08.01 2025.09.01')
        self.parser.clear_data()
        self.assertEqual(len(self.parser.currency_rate), 0)
        self.assertEqual(len(self.parser.historical_rate), 0)
        self.assertEqual(len(self.parser.rate_with_source), 0)
        self.assertEqual(len(self.parser.rate_with_fee), 0)

    @patch('builtins.open', new_callable=mock_open, read_data='"USD" "RUB" 88.50 2025.09.03 "Сбер"\n"Invalid"')
    def test_process_file_with_parser(self, mock_file):
        with patch('sys.stdout', new=StringIO()) as mocked_output:
            from file_manager import process_file
            process_file('source.txt', self.parser.parse_rate_with_source, "Курсы с источником")
            output = mocked_output.getvalue()
            self.assertTrue("Ошибка обработки строки" in output)
            self.assertTrue("RateWithSource" in output or "Курсы с источником" in output)

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_process_file_not_found(self, mock_file):
        with patch('sys.stdout', new=StringIO()) as mocked_output:
            from file_manager import process_file
            process_file('nonexistent.txt', self.parser.parse_currency_rate, "Курсы валют")
            output = mocked_output.getvalue()
            self.assertTrue("nonexistent.txt" in output and "ошибка" in output.lower())


if __name__ == '__main__':
    unittest.main()
    # python -m unittest tests.py
