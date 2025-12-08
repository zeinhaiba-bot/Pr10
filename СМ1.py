attempts = 3

while True:
    password = input("Введите пароль - ")
    if password == 'admin':
        print ("Пароль верный")
        break
    attempts -= 1
    if attempts == 0:
        print("Доступ заблокирован")
        break
    print(f"Осталось попыток {attempts}")