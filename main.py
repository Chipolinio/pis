def parse_currency_rate(input_str: str) -> dict:
    parts = input_str.strip().split()
    currency1 = parts[0].replace('"', '')
    currency2 = parts[1].replace('"', '')
    rate = float(parts[2])
    date = parts[3]
    return {"from_currency": currency1,"to_currency": currency2,"rate": rate,"date": date}
with open("1.txt", "r") as f:
    for data in f:
        print(parse_currency_rate(data))
