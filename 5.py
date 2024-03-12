a = int(input())
if a < 60:
    print("Легкий вес")
elif 64 > a >= 60:
    print("ПЕрвый полусредний вес")
elif 64 <= a < 69:
    print("ПОлусредний вес")
else:
    print("Не в категории")
