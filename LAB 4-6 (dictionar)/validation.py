def validate_day(day):
    message = ""
    try:
        day = int(day)
        assert (day in range(1, 32))
    except:
        message += "Ziua trebuie sa fie un numar natural cuprins intre 1 si 31\n"
    if len(message):
        raise Exception(message)
    return day


def validate_amount(amount):
    message = ""
    try:
        amount = int(amount)
        assert (amount > 0)
    except:
        message += "Suma trebuie sa fie un numar natural mai mare ca 0\n"
    if len(message):
        raise Exception(message)
    return amount


def validate_type(transaction_type):
    message = ""
    try:
        transaction_type = transaction_type.lower()
        assert (transaction_type in ['intrare', 'iesire'])
    except:
        message += "Tipul tranzactiei trebuie sa fie intrare sau iesire\n"
    if len(message):
        raise Exception(message)
    return transaction_type


def validate_period(start_day, end_day):
    if start_day > end_day:
        raise Exception("Ziua de sfârșit nu poate fi mai mica decât ziua de inceput.")
