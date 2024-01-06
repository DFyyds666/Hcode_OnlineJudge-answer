leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
common = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
year = int(input())
month = int(input())
day = int(input())

res = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    for i in range(1, month):
        res += leap[i]
    res += day
    print(res)
else:
    for i in range(1, month):
        res += common[i]
    res += day
    print(res)
