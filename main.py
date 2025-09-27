from file_manager import process_file
from CurrencyRateParser import CurrencyRateParser
from HistoricalRateParser import HistoricalRateParser
from RateWithSourceParser import RateWithSourceParser
from RateWithFeeParser import RateWithFeeParser

def main() -> None:
    parsers = [
        ('1.txt', CurrencyRateParser(), "Курсы валют", "currency"),
        ('2.txt', HistoricalRateParser(), "Исторические курсы", "historical"),
        ('3.txt', RateWithSourceParser(), "Курсы с источником", "with_source"),
        ('4.txt', RateWithFeeParser(), "Курсы с комиссией", "with_fee")
    ]

    all_objects = {parser[-1]: [] for parser in parsers}

    for file_path, parser, data_name, key in parsers:
        all_objects[key] = process_file(file_path, parser, data_name)

    print("=== Сводная информация ===")
    for key, objs in all_objects.items():
        print(f"Всего записей {key}: {len(objs)}")
    print(f"Всего валютных записей: {sum(len(v) for v in all_objects.values())}")

if __name__ == "__main__":
    main()
