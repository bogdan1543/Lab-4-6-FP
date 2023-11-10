from validation import *


def get_transaction_day(day):
    day = validate_day(day)
    return day


def get_transaction_amount(amount):
    amount = validate_amount(amount)
    return amount


def get_transaction_type(transaction_type):
    transaction_type = validate_type(transaction_type)
    return transaction_type


def set_transaction(day, amount, transaction_type):
    return {0: day, 1: amount, 2: transaction_type}
