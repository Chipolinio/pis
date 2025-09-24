from BaseRate import BaseRate
from CurrencyRate import CurrencyRate
from HistoricalRate import HistoricalRate
from RateWithSource import RateWithSource
from RateWithFee import RateWithFee
from Errors import ParsingError

class Parser:
    """Класс для парсинга."""
    @staticmethod
    def parse_date(date_str: str) -> tuple[str, str, str]:
        """Парсит строку с датой в формате YYYY.MM.DD"""
        parts = date_str.split(".")
        if len(parts) != 3:
            raise ParsingError(f"Неверный формат даты: {date_str}")
        return parts[0], parts[1], parts[2]

    def parse_currency_rate(self, line: str) -> CurrencyRate:
        """Парсит строку с информацией о курсе."""
        try:
            parts = line.strip().split()
            obj = CurrencyRate(
                from_currency=parts[0].replace('"', ''),
                to_currency=parts[1].replace('"', ''),
                rate=float(parts[2]),
                date=self.parse_date(parts[3])
            )
            return obj
        except Exception as e:
            raise ParsingError(f"Ошибка парсинга currency_rate: {line}") from e

    def parse_historical_rate(self, line: str) -> HistoricalRate:
        """Парсит строку с информацией о курсе."""
        try:
            parts = line.strip().split()
            obj = HistoricalRate(
                from_currency=parts[0].replace('"', ''),
                to_currency=parts[1].replace('"', ''),
                rate=float(parts[2]),
                from_date=self.parse_date(parts[3]),
                to_date=self.parse_date(parts[4])
            )
            return obj
        except Exception as e:
            raise ParsingError(f"Ошибка парсинга historical_rate: {line}") from e

    def parse_rate_with_source(self, line: str) -> RateWithSource:
        """Парсит строку с информацией о курсе."""
        try:
            parts = line.strip().split()
            obj = RateWithSource(
                from_currency=parts[0].replace('"', ''),
                to_currency=parts[1].replace('"', ''),
                rate=float(parts[2]),
                date=self.parse_date(parts[3]),
                source=parts[4].replace('"', '')
            )
            return obj
        except Exception as e:
            raise ParsingError(f"Ошибка парсинга rate_with_source: {line}") from e

    def parse_rate_with_fee(self, line: str) -> RateWithFee:
        """Парсит строку с информацией о курсе"""
        try:
            parts = line.strip().split()
            obj = RateWithFee(
                from_currency=parts[0].replace('"', ''),
                to_currency=parts[1].replace('"', ''),
                rate=float(parts[2]),
                date=self.parse_date(parts[3]),
                fee=float(parts[4])
            )
            return obj
        except Exception as e:
            raise ParsingError(f"Ошибка парсинга rate_with_fee: {line}") from e






