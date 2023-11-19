import math

n = int(input())
m = int(input())

if math.gcd(n, m) == 1:
    print("Yes")
else:
    print("No")
