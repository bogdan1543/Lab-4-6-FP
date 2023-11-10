# Initializăm lista de tranzacții și lista pentru operația "Undo"
transactions = []
previous_transactions = []


# Funcție pentru adăugarea de noi tranzacții
def add_transaction(transaction):
    transactions.append(transaction)
    previous_transactions.append(transactions[:])
    return transactions


# Funcție pentru actualizarea unei tranzacții
def update_transaction(transaction, new_transaction):
    for index, tr in enumerate(transactions):
        if tr[0] == transaction[0] and tr[1] == transaction[1] and tr[2] == transaction[2]:
            # Actualizăm tranzacția
            transactions[index] = new_transaction
            previous_transactions.append(transactions[:])
            return transactions
    raise Exception("Tranzacția nu a fost găsită pentru actualizare.")


# Funcție pentru ștergerea tranzacțiilor de la o zi specificată
def delete_by_day(day):
    transactions[:] = [t for t in transactions if t[0] != day]
    previous_transactions.append(transactions[:])
    return transactions


# Funcție pentru ștergerea tranzacțiilor dintr-o perioadă dată
def delete_by_period(start_day, end_day):
    transactions[:] = [t for t in transactions if not (start_day <= t[0] <= end_day)]
    previous_transactions.append(transactions[:])
    return transactions


# Funcție pentru ștergerea tranzacțiilor de un anumit tip
def delete_by_type(transaction_type):
    transactions[:] = [t for t in transactions if t[2] != transaction_type]
    previous_transactions.append(transactions[:])
    return transactions


# Funcție pentru tipărirea tranzacțiilor cu sume mai mari decât o sumă dată
def print_greater_than_amount(amount):
    filtered_transactions = [t for t in transactions if t[1] > amount]
    return filtered_transactions


# Funcție pentru tipărirea tranzacțiilor efectuate înainte de o zi și mai mari decât o sumă
def print_before_day_and_greater_than_amount(day, amount):
    filtered_transactions = [t for t in transactions if t[0] < day and t[1] > amount]
    return filtered_transactions


# Funcție pentru tipărirea tranzacțiilor de un anumit tip
def print_by_type(transaction_type):
    filtered_transactions = [t for t in transactions if t[2] == transaction_type]
    return filtered_transactions


# Funcție pentru calcularea sumei totale a tranzacțiilor de un anumit tip
def total_by_type(transaction_type):
    total = sum(t[1] for t in transactions if t[2] == transaction_type)
    print(f"Totalul tranzacțiilor de tipul {transaction_type}: {total}")
    return total


# Funcție pentru calcularea soldului contului la o dată specificată
def account_balance(day):
    balance = sum(t[1] for t in transactions if t[0] <= day and t[2] == 'intrare')
    print(f"Soldul contului la ziua {day}: {balance}")
    return balance


# Funcție pentru tipărirea tranzacțiilor de un anumit tip ordonate după sumă
def print_ordered_by_amount(transaction_type):
    filtered_transactions = sorted([t for t in transactions if t[2] == transaction_type], key=lambda t: t[1])
    return filtered_transactions


# Funcție pentru eliminarea tuturor tranzacțiilor de un anumit tip
def remove_by_type(transaction_type):
    filtered_transactions = [t for t in transactions if t[2] != transaction_type]
    return filtered_transactions


# Funcție pentru eliminarea tranzacțiilor mai mici decât o sumă dată cu un anumit tip
def remove_by_type_and_amount(amount, transaction_type):
    transactions[:] = [t for t in transactions if not (t[2] == transaction_type and t[1] < amount)]
    previous_transactions.append(transactions[:])
    return transactions


# Funcție pentru refacerea ultimei operații
def undo_last_operation():
    if previous_transactions:
        previous_transactions.pop()
        transactions[:] = previous_transactions
    return transactions
