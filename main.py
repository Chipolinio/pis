def parse_currency_rate(input_str: str) -> dict:
    """Парсит строку с информацией о курсе.

        Args:            input_str: Строка для парсинга в формате "from_currency" "to_currency" "rate" "date"
        Returns:            Словарь с ключами: from_currency to_currency rate date    """
    parts = input_str.strip().split()
    currency1 = parts[0].replace('"', '')
    currency2 = parts[1].replace('"', '')
    rate = float(parts[2])
    date = parts[3]

    return {"type": "currency_rate",
            "from_currency": currency1,
            "to_currency": currency2,
            "rate": rate,
            "date": date}


def parse_historical_rate(input_str: str) -> dict:
    """Парсит строку с информацией о курсе.

        Args:            input_str: Строка для парсинга в формате "from_currency" "to_currency" "rate" "date1" "date2"
        Returns:            Словарь с ключами: from_currency to_currency rate from_date to_date    """
    parts = input_str.strip().split()
    currency1 = parts[0].replace('"', '')
    currency2 = parts[1].replace('"', '')
    rate = float(parts[2])
    date1 = parts[3]
    date2 = parts[4]

    return {"type": "historical_rate",
            "from_currency": currency1,
            "to_currency": currency2,
            "rate": rate,
            "from_date": date1,
            "to_date": date2}


def parse_rate_with_source(input_str: str) -> dict:
    """Парсит строку с информацией о курсе.

        Args:            input_str: Строка для парсинга в формате "from_currency" "to_currency" "rate" "date" "source"
        Returns:            Словарь с ключами: from_currency to_currency rate date source    """
    parts = input_str.strip().split()
    currency1 = parts[0].replace('"', '')
    currency2 = parts[1].replace('"', '')
    rate = float(parts[2])
    date = parts[3]
    source = parts[4].replace('"', '')

    return {"type": "rate_with_source",
            "from_currency": currency1,
            "to_currency": currency2,
            "rate": rate,
            "date": date,
            "source": source}


def parse_rate_with_fee(input_str: str) -> dict:
    """Парсит строку с информацией о курсе.

        Args:            input_str: Строка для парсинга в формате "from_currency" "to_currency" "rate" "date" "fee"
        Returns:            Словарь с ключами: from_currency to_currency rate date fee    """
    parts = input_str.strip().split()
    currency1 = parts[0].replace('"', '')
    currency2 = parts[1].replace('"', '')
    rate = float(parts[2])
    date = parts[3]
    fee = float(parts[4])

    return {"type": "rate_with_fee",
            "from_currency": currency1,
            "to_currency": currency2,
            "rate": rate,
            "date": date,
            "fee": fee}