from CurrencyRate import CurrencyRate
from Errors import ParsingError
from BaseParser import BaseParser

class CurrencyRateParser(BaseParser):
    def parse(self, line: str) -> CurrencyRate:
        try:
            parts = line.strip().split()
            return CurrencyRate(
                from_currency=parts[0].replace('"', ''),
                to_currency=parts[1].replace('"', ''),
                rate=float(parts[2]),
                date=self.parse_date(parts[3])
            )
        except Exception as e:
            raise ParsingError(f"Ошибка парсинга currency_rate: {line}") from e
