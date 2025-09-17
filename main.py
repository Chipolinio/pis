from parse import parse_currency_rate, parse_historical_rate, parse_rate_with_source, parse_rate_with_fee
from file_manaher import parse_file


def main() -> None:
    file_parsers = [
        ("1.txt", parse_currency_rate),
        ("2.txt", parse_historical_rate),
        ("3.txt", parse_rate_with_source),
        ("4.txt", parse_rate_with_fee),
    ]

    for file_path, func in file_parsers:
        objects = parse_file(file_path, func)
        for obj in objects:
            print(obj)

    print()


if __name__ == "__main__":
    main()