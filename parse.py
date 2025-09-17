def parse_currency_rate(input_str: str) -> dict:
    """Парсит строку с информацией о курсе.

        Args:            input_str: Строка для парсинга в формате "from_currency" "to_currency" "rate" "date"
        Returns:            Словарь с ключами: from_currency to_currency rate date    """
    parts = input_str.strip().split()
    currency1 = parts[0].replace('"', '')
    currency2 = parts[1].replace('"', '')
    rate = float(parts[2])
    date = parse_data(parts[3])

    return {"type": "currency_rate",
            "from_currency": currency1,
            "to_currency": currency2,
            "rate": rate,
            "YY": date[0],
            "mm": date[1],
            "dd": date[2]}


def parse_historical_rate(input_str: str) -> dict:
    """Парсит строку с информацией о курсе.

        Args:            input_str: Строка для парсинга в формате "from_currency" "to_currency" "rate" "date1" "date2"
        Returns:            Словарь с ключами: from_currency to_currency rate from_date to_date    """
    parts = input_str.strip().split()
    currency1 = parts[0].replace('"', '')
    currency2 = parts[1].replace('"', '')
    rate = float(parts[2])
    date1 = parse_data(parts[3])
    date2 = parse_data(parts[4])

    return {"type": "historical_rate",
            "from_currency": currency1,
            "to_currency": currency2,
            "rate": rate,
            "from_YY": date1[0],
            "from_mm": date1[1],
            "from_dd": date1[2],
            "to_YY": date2[0],
            "to_mm": date2[1],
            "todd": date2[2]}


def parse_rate_with_source(input_str: str) -> dict:
    """Парсит строку с информацией о курсе.

        Args:            input_str: Строка для парсинга в формате "from_currency" "to_currency" "rate" "date" "source"
        Returns:            Словарь с ключами: from_currency to_currency rate date source    """
    parts = input_str.strip().split()
    currency1 = parts[0].replace('"', '')
    currency2 = parts[1].replace('"', '')
    rate = float(parts[2])
    date = parse_data(parts[3])
    source = parts[4].replace('"', '')

    return {"type": "rate_with_source",
            "from_currency": currency1,
            "to_currency": currency2,
            "rate": rate,
            "YY": date[0],
            "mm": date[1],
            "dd": date[2],
            "source": source}

def parse_data(data: str) -> (str, str, str):
    """Парсит строку с датой.

        Args:            input_str: Строка для парсинга в формате "date"
        Returns:            Кортеж со строками (YY, mm, dd)"""
    data = data.split(".")
    year = data[0]
    mm = data[1]
    day = data[2]
    return (year, mm, day)


def parse_rate_with_fee(input_str: str) -> dict:
    """Парсит строку с информацией о курсе.

        Args:            input_str: Строка для парсинга в формате "from_currency" "to_currency" "rate" "date" "fee"
        Returns:            Словарь с ключами: from_currency to_currency rate date fee    """
    parts = input_str.strip().split()
    currency1 = parts[0].replace('"', '')
    currency2 = parts[1].replace('"', '')
    rate = float(parts[2])
    date = parse_data(parts[3])
    fee = float(parts[4])

    return {"type": "rate_with_fee",
            "from_currency": currency1,
            "to_currency": currency2,
            "rate": rate,
            "YY": date[0],
            "mm": date[1],
            "dd": date[2],
            "fee": fee}