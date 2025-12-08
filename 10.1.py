while True:
    password = input("Введите пароль - ")
    if password == '4590':
        print ("Пароль верный")
        break
    else:
        print("Ошибка. Попробуйте еще раз.")
print(f"Доступ разрешен")