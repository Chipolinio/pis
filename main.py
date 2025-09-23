from file_manager import process_file
from Parser import Parser

def main() -> None:
    """Основаная функция"""
    parser = Parser()
    file_parsers = [
        ('1.txt', parser.parse_currency_rate, "Курсы валют"),
        ('2.txt', parser.parse_historical_rate, "Исторические курсы"),
        ('3.txt', parser.parse_rate_with_source, "Курсы с источником"),
        ('4.txt', parser.parse_rate_with_fee, "Курсы с комиссией")
    ]

    for file_path, parser_func, data_name in file_parsers:
        process_file(file_path, parser_func, data_name)

    print("=== Сводная информация ===")
    print(f"Всего записей с обычным курсом: {len(parser.currency_rate)}")
    print(f"Всего записей за диапазон дат: {len(parser.historical_rate)}")
    print(f"Всего записей с источником: {len(parser.rate_with_source)}")
    print(f"Всего записей с комиссией: {len(parser.rate_with_fee)}")
    print(f"Всего валютных записей: {len(parser.get_all_value())}")


if __name__ == "__main__":
    main()