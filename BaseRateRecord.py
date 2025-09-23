from dataclasses import dataclass

@dataclass
class RateRecord:
    """Базовый класс для всех валютных записей"""
    from_currency: str
    to_currency: str
    rate: float
    date: tuple[str, str, str]

    def __post_init__(self):
        if not self.from_currency.strip():
            raise ValueError("Название исходной валюты не может быть пустым")
        if not self.to_currency.strip():
            raise ValueError("Название целевой валюты не может быть пустым")
        if self.rate < 0:
            raise ValueError("Курс валюты не может быть отрицательным")
        if len(self.date) != 3:
            raise ValueError("Дата должна быть в формате (YYYY, MM, DD)")

    def __str__(self) -> str:
        yy, mm, dd = self.date
        return f"{self.from_currency} → {self.to_currency}: {self.rate:.2f} (дата {yy}-{mm}-{dd})"