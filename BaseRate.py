from dataclasses import dataclass
from Errors import ValidationError


@dataclass
class BaseRate:
    """Общий базовый класс для валютных записей."""
    from_currency: str
    to_currency: str
    rate: float

    def __post_init__(self):
        if not self.from_currency or not self.to_currency:
            raise ValidationError("Валютные коды не могут быть пустыми")
        if len(self.from_currency) != 3 or len(self.to_currency) != 3:
            raise ValidationError("Код валюты не равен 3")
        if self.rate < 0:
            raise ValidationError("Курс валюты не может быть отрицательным")