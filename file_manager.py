from typing import List, Any
from Errors import ParsingError

def read_file_lines(file_path: str) -> List[str]:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        raise ParsingError(f"Файл {file_path} не найден")
    except Exception as e:
        raise ParsingError(f"Ошибка при чтении файла {file_path}: {e}")

def process_file(file_path: str, parser, data_name: str) -> List[Any]:
    result = []
    try:
        lines = read_file_lines(file_path)
        print(f"=== {data_name} из {file_path} ===")
        for line in lines:
            try:
                obj = parser.parse(line)
                result.append(obj)
                print(obj)
            except ParsingError as e:
                print(f"Ошибка обработки строки: {e}")
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")
        print()
        return result
    except ParsingError as e:
        print(f"Ошибка: {e}")
        return []
