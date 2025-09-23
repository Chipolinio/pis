class ParsingError(Exception):
    """Ошибка при парсинге входных данных"""


class ValidationError(Exception):
    """Ошибка валидации данных (например, неверная дата или валюта)"""
