month = int(input())
if month == 2:
    days = 28
elif month in [4, 6, 9, 11]:
    days = 30
else:
    days = 31
print(days)