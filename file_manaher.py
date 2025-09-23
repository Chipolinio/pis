def read_lines(file_path: str) -> list:
    """Читает все строки из файла.

    Args:        file_path: Путь к файлу
    Returns:        Список строк файла    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()


def parse_file(file_path: str, parser_func) -> list[dict] | None:
    """Обрабатывает файл с использованием указанной функции-парсера.

    Args:        file_path: Путь к файлу для обработки        parser_func: Функция для парсинга строк    """
    results = []
    try:
        for line in read_lines(file_path):
            line = line.strip()
            if line:
                results.append(parser_func(line))

        return results

    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден")
    except Exception as e:
        print(f"Ошибка при обработке файла {file_path}: {e}")

