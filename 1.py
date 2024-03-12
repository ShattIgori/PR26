a = int(input())
a1 = int(input())
a2 = int(input())

if a < a1 < a2 or a2 < a1 < a:
    print(a1)

elif a1 < a < a2 or a2 < a < a1:
    print(a)

else:
    print(c)
