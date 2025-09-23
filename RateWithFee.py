from dataclasses import dataclass
from DatedRate import DatedRate
from errors import ValidationError

@dataclass
class RateWithFee(DatedRate):
    """Курс валюты с комиссией"""
    fee: float

    def __post_init__(self):
        super().__post_init__()
        if self.fee < 0:
            raise ValidationError("Комиссия не может быть отрицательной")