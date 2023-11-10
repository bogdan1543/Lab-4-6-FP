from service import *


def test_validate_day():
    day = "21"
    assert (validate_day(day) == int(day))
    day = "50"
    try:
        validate_day(day)
        assert (False)
    except:
        pass
    day = "abc"
    try:
        validate_day(day)
        assert (False)
    except:
        pass


def test_validate_amount():
    amount = "2345"
    assert (validate_amount(amount) == int(amount))
    amount = "-23"
    try:
        validate_amount(amount)
        assert (False)
    except:
        pass
    amount = "abc"
    try:
        validate_amount(amount)
        assert (False)
    except:
        pass


def test_validate_type():
    transaction_type = "intrare"
    assert (validate_type(transaction_type) == transaction_type.lower())
    transaction_type = "abc"
    try:
        validate_type(transaction_type)
        assert (False)
    except:
        pass
    transaction_type = "2"
    try:
        validate_type(transaction_type)
        assert (False)
    except:
        pass


def test_validate_period():
    start_day = "20"
    end_day = "25"
    assert (validate_period(start_day, end_day) == None)
    start_day = "20"
    end_day = "15"
    try:
        validate_period(start_day, end_day)
        assert (False)
    except:
        pass


def test_service_add_transaction():
    service_add_transaction(3, 200, 'intrare')
    service_add_transaction(2, 200, 'iesire')
    service_add_transaction(20, 420, 'intrare')

    assert service_add_transaction(3, 200, 'intrare') == [[3, 200, 'intrare'], [2, 200, 'iesire'], [20, 420, 'intrare'],
                                                          [3, 200, 'intrare']]

    try:
        service_add_transaction(0, 0, 0)
        assert False
    except:
        pass
    try:
        service_add_transaction(2, 0, 'intrare')
        assert False
    except:
        pass
    try:
        service_add_transaction(2, 24, 'abc')
        assert False
    except:
        pass
    transactions.clear()


def test_service_update_transaction():
    service_add_transaction(3, 200, 'intrare')
    service_add_transaction(2, 200, 'iesire')
    service_add_transaction(20, 420, 'intrare')
    assert (service_update_transaction(3, 200, 'intrare', 3, 500, 'intrare') == [[3, 500, 'intrare'],
                                                                                 [2, 200, 'iesire'],
                                                                                 [20, 420, 'intrare']])
    try:
        service_update_transaction(0, 0, 0, 0, 0, 0)
        assert False
    except:
        pass
    try:
        service_update_transaction(20, 2020, 'intrare', 15, 2000, 'iesire')
        assert False
    except:
        pass


def test_service_delete_by_day():
    assert service_delete_by_day(3) == [[2, 200, 'iesire'], [20, 420, 'intrare']]
    try:
        service_delete_by_day("a")
        assert False
    except:
        pass
    # transactions.clear()


def test_service_delete_by_period():
    service_add_transaction(3, 200, 'iesire')
    assert service_delete_by_period(2, 3) == [[20, 420, 'intrare']]
    try:
        service_delete_by_period("abc", 5)
        assert False
    except:
        pass
    try:
        service_delete_by_period(15, 9)
        assert False
    except:
        pass


def test_service_delete_by_type():
    service_add_transaction(3, 200, 'intrare')
    service_add_transaction(2, 200, 'iesire')
    assert service_delete_by_type('intrare') == [[2, 200, 'iesire']]
    try:
        service_delete_by_type('int')
        assert False
    except:
        pass


def test_service_print_greater_than_amount():
    service_add_transaction(3, 200, 'intrare')
    service_add_transaction(20, 420, 'intrare')
    assert service_print_greater_than_amount(200) == [[20, 420, 'intrare']]
    try:
        service_print_greater_than_amount(-23)
        assert False
    except:
        pass


def test_service_print_before_day_and_greater_than_amount():
    assert service_print_before_day_and_greater_than_amount(3, 100) == [[2, 200, 'iesire']]
    try:
        service_print_before_day_and_greater_than_amount("a", 100)
        assert False
    except:
        pass
    try:
        service_print_before_day_and_greater_than_amount("abc", "def")
        assert False
    except:
        pass


def test_service_print_by_type():
    assert service_print_by_type('intrare') == [[3, 200, 'intrare'], [20, 420, 'intrare']]
    try:
        service_print_by_type(2)
        assert False
    except:
        pass
    try:
        service_print_by_type('intr')
        assert False
    except:
        pass


def test_service_total_by_type():
    assert service_total_by_type('intrare') == 620
    try:
        service_total_by_type(2)
        assert False
    except:
        pass
    try:
        service_total_by_type('intr')
        assert False
    except:
        pass


def test_service_account_balance():
    assert service_account_balance(3) == 200
    assert service_account_balance(2) == 0
    try:
        service_account_balance("abc")
        assert False
    except:
        pass
    try:
        service_account_balance(40)
        assert False
    except:
        pass


def test_service_print_ordered_by_amount():
    service_add_transaction(5, 100, 'intrare')
    assert service_print_ordered_by_amount('intrare') == [[5, 100, 'intrare'], [3, 200, 'intrare'],
                                                          [20, 420, 'intrare']]
    try:
        service_print_ordered_by_amount(2)
        assert False
    except:
        pass
    try:
        service_print_ordered_by_amount('intr')
        assert False
    except:
        pass


def test_service_remove_by_type():
    assert service_remove_by_type('intrare') == [[2, 200, 'iesire']]
    assert service_remove_by_type('iesire') == [[3, 200, 'intrare'], [20, 420, 'intrare'], [5, 100, 'intrare']]
    try:
        service_remove_by_type(2)
        assert False
    except:
        pass
    try:
        service_remove_by_type('intr')
        assert False
    except:
        pass


def test_service_remove_by_type_and_amount():
    assert service_remove_by_type_and_amount(200, 'intrare') == [[2, 200, 'iesire'], [20, 420, 'intrare']]
    assert service_remove_by_type_and_amount(10, 'iesire') == [[2, 200, 'iesire'], [3, 200, 'intrare'],
                                                               [20, 420, 'intrare'], [5, 100, 'intrare']]
    try:
        service_remove_by_type_and_amount("a", 100)
        assert False
    except:
        pass
    try:
        service_remove_by_type_and_amount(152, "def")
        assert False
    except:
        pass


transactions.clear()


def check_tests():
    test_validate_day()
    test_validate_amount()
    test_validate_type()
    test_validate_period()
    test_service_add_transaction()
    test_service_update_transaction()
    test_service_delete_by_day()
    test_service_delete_by_period()
    test_service_delete_by_type()
    test_service_print_greater_than_amount()
    test_service_print_before_day_and_greater_than_amount()
    test_service_print_by_type()
    test_service_total_by_type()
    test_service_account_balance()
    test_service_print_ordered_by_amount()
    test_service_remove_by_type()
    test_service_remove_by_type_and_amount()
