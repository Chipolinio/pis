from dataclasses import dataclass
from DatedRate import DatedRate

@dataclass
class CurrencyRate(DatedRate):
    """Обычный курс валюты"""
    pass
