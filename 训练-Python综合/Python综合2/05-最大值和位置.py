n = [3, 9, 1, 6, 2, 8]

append_num = int(input())

n.append(append_num)

print(max(n))
for i in range(0, len(n)):
    if n[i] == max(n):
        print(i)
        break
