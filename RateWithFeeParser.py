from RateWithFee import RateWithFee
from Errors import ParsingError
from BaseParser import BaseParser

class RateWithFeeParser(BaseParser):
    def parse(self, line: str) -> RateWithFee:
        try:
            parts = line.strip().split()
            return RateWithFee(
                from_currency=parts[0].replace('"', ''),
                to_currency=parts[1].replace('"', ''),
                rate=float(parts[2]),
                date=self.parse_date(parts[3]),
                fee=float(parts[4])
            )
        except Exception as e:
            raise ParsingError(f"Ошибка парсинга rate_with_fee: {line}") from e
