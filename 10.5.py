balance = 1000
while True:
    print("="*50)
    print("1. Узнать баланс")
    print("2. Снять 100 рублей")
    print("3. Положить 100 рублей")
    print("4. Выход")
    print("="*50)
    choise = input("Введите номер операции (1-4): ")
    if choise == "1":
        print(f"Ваш баланс: {balance}")
    elif choise == "2":
        if balance>=100:
            balance -= 100
            print("Снято 100 рублей")
        else:
            print("Недостаточно средств")
    elif choise == "3":
        balance += 100
        print("Внесено 100 рублей")
    elif choise == "4":
        print("Др свидания")
        break
    else:
        print("Неверная команда")