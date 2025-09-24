from typing import List, Callable, Any
from Errors import ParsingError
from CurrencyRate import CurrencyRate
from HistoricalRate import HistoricalRate
from RateWithSource import RateWithSource
from RateWithFee import RateWithFee

def read_file_lines(file_path: str) -> List[str]:
    """Читает все строки из файла, пропуская пустые.

    Args:
        file_path: путь к файлу

    Returns:
        список строк файла
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        raise ParsingError(f"Файл {file_path} не найден")
    except Exception as e:
        raise ParsingError(f"Ошибка при чтении файла {file_path}: {e}")


def process_file(file_path: str, parser_func: Callable[[str], Any], data_name: str) -> List[Any]:
    """Обрабатывает файл с использованием метода парсера."""
    result = []
    try:
        lines = read_file_lines(file_path)
        print(f"=== {data_name} из {file_path} ===")
        for line in lines:
            try:
                obj = parser_func(line)
                result.append(obj)
                print(obj)
            except ParsingError as e:
                print(f"Ошибка обработки строки в файле {file_path}: {e}")
            except Exception as e:
                print(f"Неожиданная ошибка при обработке строки '{line}': {e}")
        print()
        return result
    except ParsingError as e:
        print(f"Ошибка: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка при обработке файла {file_path}: {e}")
        return []



