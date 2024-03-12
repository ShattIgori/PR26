a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a2 > b1 or a1 > b2:
    print("пустое множество")
else:
    start = max(a1, a2)
    end = min(b1, b2)

    if start == end:
        print(start)
    else:
        print(start, end)