from dataclasses import dataclass
from errors import ValidationError
from datetime import datetime
from BaseRate import BaseRate

@dataclass
class DatedRate(BaseRate):
    """Курс валюты с одной датой"""
    date: tuple[str, str, str]

    def __post_init__(self):
        super().__post_init__()
        self._validate_date(self.date)

    @staticmethod
    def _validate_date(date_tuple: tuple[str, str, str]) -> None:
        if len(date_tuple) != 3:
            raise ValidationError("Дата должна быть в формате (YYYY, MM, DD)")
        year, month, day = date_tuple
        try:
            datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
        except ValueError:
            raise ValidationError(f"Некорректная дата: {date_tuple}")
