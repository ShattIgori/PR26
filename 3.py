num1 = int(input())
znak = input()
num2 = int(input())

if znak == "+":
    print(num1 + num2)
elif znak == "-":
    print(num1 - num2)
elif znak == "*":
    print(num1 * num2)
elif znak == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("На ноль делить нельзя!")
else:
    print("Неверная операция")