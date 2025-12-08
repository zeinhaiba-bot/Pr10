num = 1

while True:
    num_1 = int(input("Введите число>>>"))
    if num_1 < 0:
        break
    num = num_1 * num

print(f"Произведение - {num}")