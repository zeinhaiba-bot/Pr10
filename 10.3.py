number = 0
while True:
    num = int(input("Введите числа: "))
    if num == 0:
        break
    if num > number:
        number = num
print(number)