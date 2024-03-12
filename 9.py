a = int(input())

if a == 0:
    print("Зеленый")
elif 1 <= a <= 10:
    if a % 2 == 0:
        print("Черный")
    else:
        print("Красный")
elif 11 <= a <= 18:
    if a % 2 == 0:
        print("Красный")
    else:
        print("Черный")
elif 19 <= a <= 28:
    if a % 2 == 0:
        print("Черный")
    else:
        print("Красный")
elif 29 <= a <= 36:
    if a % 2 == 0:
        print("Красный")
    else:
        print("Черный")
else:
    print("ошибка ввода")