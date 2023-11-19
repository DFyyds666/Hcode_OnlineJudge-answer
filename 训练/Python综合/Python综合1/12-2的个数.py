n = int(input())

res = 0
for i in range(1, n + 1):
    tmp = i
    while tmp > 0:
        if tmp % 10 == 2:
            res += 1
        tmp //= 10

print(res)
