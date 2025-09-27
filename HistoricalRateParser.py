from HistoricalRate import HistoricalRate
from Errors import ParsingError
from BaseParser import BaseParser

class HistoricalRateParser(BaseParser):
    def parse(self, line: str) -> HistoricalRate:
        try:
            parts = line.strip().split()
            return HistoricalRate(
                from_currency=parts[0].replace('"', ''),
                to_currency=parts[1].replace('"', ''),
                rate=float(parts[2]),
                from_date=self.parse_date(parts[3]),
                to_date=self.parse_date(parts[4])
            )
        except Exception as e:
            raise ParsingError(f"Ошибка парсинга historical_rate: {line}") from e
