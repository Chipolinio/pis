from RateWithSource import RateWithSource
from Errors import ParsingError
from BaseParser import BaseParser

class RateWithSourceParser(BaseParser):
    def parse(self, line: str) -> RateWithSource:
        try:
            parts = line.strip().split()
            return RateWithSource(
                from_currency=parts[0].replace('"', ''),
                to_currency=parts[1].replace('"', ''),
                rate=float(parts[2]),
                date=self.parse_date(parts[3]),
                source=" ".join(parts[4:]).replace('"', '')
            )
        except Exception as e:
            raise ParsingError(f"Ошибка парсинга rate_with_source: {line}") from e
