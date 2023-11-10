from service import *


# Funcție pentru afișarea meniului
def print_menu():
    print("\nAlege o opțiune:")
    print("1. Adăugare de noi tranzacții")
    print("2. Ștergere")
    print("3. Căutări")
    print("4. Rapoarte")
    print("5. Filtrare")
    print("6. Undo")
    print("7. Ieșire")


# Funcție principală pentru gestionarea meniului
def consola():
    while True:
        try:
            print_menu()
            choice = input("Opțiune: ")
            if choice == '1':
                print("1. Adăuga tranzacții")
                print("2. Actualizare tranzacție")
                add_or_update_choice = input("Opțiune: ")
                if add_or_update_choice == '1':
                    day = input("Ziua: ")
                    amount = input("Suma: ")
                    transaction_type = input("Tip (intrare/iesire): ")
                    print(service_add_transaction(day, amount, transaction_type))

                elif add_or_update_choice == '2':
                    day = input("Ziua: ")
                    amount = input("Suma: ")
                    transaction_type = input("Tip (intrare/iesire): ")
                    new_day = input("Ziua noua: ")
                    new_amount = input("Suma noua: ")
                    new_transaction_type = input("Tip nou (intrare/iesire): ")
                    print(service_update_transaction(day, amount, transaction_type, new_day, new_amount,
                                                     new_transaction_type))
            elif choice == '2':
                print("1. Șterge toate tranzacțiile de la ziua specificată")
                print("2. Șterge tranzacțiile dintr-o perioadă dată")
                print("3. Șterge toate tranzacțiile de un anumit tip")
                delete_choice = input("Opțiune: ")
                if delete_choice == '1':
                    day = input("Ziua: ")
                    print(service_delete_by_day(day))
                elif delete_choice == '2':
                    start_day = input("De la: ")
                    end_day = input("Pana la: ")
                    print(service_delete_by_period(start_day, end_day))
                elif delete_choice == '3':
                    transaction_type = input("Tip (intrare/iesire): ")
                    print(service_delete_by_type(transaction_type))
            elif choice == '3':
                print("1. Tipărește tranzacțiile cu sume mai mari decât o sumă dată")
                print("2. Tipărește toate tranzacțiile efectuate înainte de o zi și mai mari decât o sumă")
                print("3. Tipărește tranzacțiile de un anumit tip")
                search_choice = input("Opțiune: ")
                if search_choice == '1':
                    amount = input("Suma: ")
                    print(service_print_greater_than_amount(amount))
                elif search_choice == '2':
                    day = input("Ziua: ")
                    amount = input("Suma: ")
                    print(service_print_before_day_and_greater_than_amount(day, amount))
                elif search_choice == '3':
                    transaction_type = input("Tip (intrare/iesire): ")
                    print(service_print_by_type(transaction_type))
            elif choice == '4':
                print("1. Suma totală a tranzacțiilor de un anumit tip")
                print("2. Soldul contului la o dată specificată")
                print("3. Tipărește toate tranzacțiile de un anumit tip ordonat după sumă")
                report_choice = input("Opțiune: ")
                if report_choice == '1':
                    transaction_type = input("Tip (intrare/iesire): ")
                    print(service_total_by_type(transaction_type))
                elif report_choice == '2':
                    day = input("Ziua: ")
                    print(service_account_balance(day))
                elif report_choice == '3':
                    transaction_type = input("Tip (intrare/iesire): ")
                    print(service_print_ordered_by_amount(transaction_type))
            elif choice == '5':
                print("1. Elimină toate tranzacțiile de un anumit tip")
                print("2. Elimină toate tranzacțiile mai mici decât o sumă dată cu un anumit tip")
                filter_choice = input("Opțiune: ")
                if filter_choice == '1':
                    transaction_type = input("Tip (intrare/iesire): ")
                    print(service_remove_by_type(transaction_type))
                elif filter_choice == '2':
                    amount = input("Suma: ")
                    transaction_type = input("Tip (intrare/iesire): ")
                    print(service_remove_by_type_and_amount(amount, transaction_type))
            elif choice == '6':
                print(service_undo_last_operation())
            elif choice == '7':
                break
            else:
                print("Opțiune invalidă!")
        except Exception as ex:
            print(f"Erori: {ex}")
