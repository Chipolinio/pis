from file_manager import process_file
from Parser import Parser

def main() -> None:
    """Основная функция"""
    parser = Parser()
    all_objects = {
        "currency": [],
        "historical": [],
        "with_source": [],
        "with_fee": []
    }

    file_parsers = [
        ('1.txt', parser.parse_currency_rate, "Курсы валют", "currency"),
        ('2.txt', parser.parse_historical_rate, "Исторические курсы", "historical"),
        ('3.txt', parser.parse_rate_with_source, "Курсы с источником", "with_source"),
        ('4.txt', parser.parse_rate_with_fee, "Курсы с комиссией", "with_fee")
    ]

    for file_path, parser_func, data_name, key in file_parsers:
        all_objects[key] = process_file(file_path, parser_func, data_name)

    print("=== Сводная информация ===")
    print(f"Всего записей с обычным курсом: {len(all_objects['currency'])}")
    print(f"Всего записей за диапазон дат: {len(all_objects['historical'])}")
    print(f"Всего записей с источником: {len(all_objects['with_source'])}")
    print(f"Всего записей с комиссией: {len(all_objects['with_fee'])}")
    total = sum(len(v) for v in all_objects.values())
    print(f"Всего валютных записей: {total}")



if __name__ == "__main__":
    main()