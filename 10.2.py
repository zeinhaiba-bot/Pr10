print("ведите три целых числа числа в строгом возрастании")
while True:
    num1 = int(input("Первое число: "))
    break
while True:
    num2 =  int(input("Второе число: "))
    if num2 > num1:
        break
    else:
        print("Второе число должно быть больше предыдущего. Введите заново.")
while True:
    num3 = int(input("Третье число: "))
    if num3 > num2:
        break
    else:
        print("Ошибка.Третье число должно быть больше предыдущего. Введите заново.")
print("Последовательность принята")