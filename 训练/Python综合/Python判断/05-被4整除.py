n = int(input())

flag = 0
for i in range(1, n + 1):
    if i % 4 == 0:
        print(i)
        flag = 1

if flag == 0:
    print(0)
