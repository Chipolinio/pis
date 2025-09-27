from Errors import ParsingError

class BaseParser:
    """Базовый класс для парсеров."""

    @staticmethod
    def parse_date(date_str: str) -> tuple[str, str, str]:
        """Парсит строку даты вида YYYY.MM.DD → (YYYY, MM, DD)."""
        parts = date_str.split(".")
        if len(parts) != 3:
            raise ParsingError(f"Неверный формат даты: {date_str}")
        return parts[0], parts[1], parts[2]
