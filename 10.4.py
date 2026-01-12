basket = 0
while True:
    price = int(input("Введите цену товара: "))
    if price == 0:
        break
    if price < 0:
        print("Такой цены нет.")
        continue
    basket += price
    if basket>1000:
        basket = basket*0.9
print(f"Сумма: {basket}")