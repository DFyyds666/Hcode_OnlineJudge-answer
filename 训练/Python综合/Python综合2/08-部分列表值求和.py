n = [3, 9, 1, 6, 2, 8]

insert_num = int(input())

n.insert(4, insert_num)
n.sort(reverse=True)

res = sum(n[1:len(n)-2])

print(res)
