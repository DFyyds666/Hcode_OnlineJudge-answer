SPEED = 7 * 5

n = int(input())

res = 0
while n > 0:
    n -= SPEED
    res += 1

print(res)
