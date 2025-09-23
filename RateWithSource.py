from dataclasses import dataclass
from DatedRate import DatedRate
from errors import ValidationError

@dataclass
class RateWithSource(DatedRate):
    source: str

    def __post_init__(self):
        super().__post_init__()
        if not self.source or not self.source.strip():
            raise ValidationError("Источник не может быть пустым")
