from repository import *
from domain import *


def service_add_transaction(day, amount, transaction_type):
    day = get_transaction_day(day)
    amount = get_transaction_amount(amount)
    transaction_type = get_transaction_type(transaction_type)
    transaction = set_transaction(day, amount, transaction_type)
    return add_transaction(transaction)


def service_update_transaction(day, amount, transaction_type, new_day, new_amount, new_transaction_type):
    day = get_transaction_day(day)
    amount = get_transaction_amount(amount)
    transaction_type = get_transaction_type(transaction_type)
    new_day = get_transaction_day(new_day)
    new_amount = get_transaction_amount(new_amount)
    new_transaction_type = get_transaction_type(new_transaction_type)
    transaction = set_transaction(day, amount, transaction_type)
    new_transaction = set_transaction(new_day, new_amount, new_transaction_type)
    return update_transaction(transaction, new_transaction)


def service_delete_by_day(day):
    day = get_transaction_day(day)
    return delete_by_day(day)


def service_delete_by_period(start_day, end_day):
    start_day = get_transaction_day(start_day)
    end_day = get_transaction_day(end_day)
    validate_period(start_day, end_day)
    return delete_by_period(start_day, end_day)


def service_delete_by_type(transaction_type):
    transaction_type = get_transaction_type(transaction_type)
    return delete_by_type(transaction_type)


def service_print_greater_than_amount(amount):
    amount = get_transaction_amount(amount)
    return print_greater_than_amount(amount)


def service_print_before_day_and_greater_than_amount(day, amount):
    day = get_transaction_day(day)
    amount = get_transaction_amount(amount)
    return print_before_day_and_greater_than_amount(day, amount)


def service_print_by_type(transaction_type):
    transaction_type = get_transaction_type(transaction_type)
    return print_by_type(transaction_type)


def service_total_by_type(transaction_type):
    transaction_type = get_transaction_type(transaction_type)
    return total_by_type(transaction_type)


def service_account_balance(day):
    day = get_transaction_day(day)
    return account_balance(day)


def service_print_ordered_by_amount(transaction_type):
    transaction_type = get_transaction_type(transaction_type)
    return print_ordered_by_amount(transaction_type)


def service_remove_by_type(transaction_type):
    transaction_type = get_transaction_type(transaction_type)
    return remove_by_type(transaction_type)


def service_remove_by_type_and_amount(amount, transaction_type):
    transaction_type = get_transaction_type(transaction_type)
    amount = get_transaction_amount(amount)
    return remove_by_type_and_amount(amount, transaction_type)


def service_undo_last_operation():
    return undo_last_operation()
