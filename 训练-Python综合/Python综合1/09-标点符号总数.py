string = input()

res = 0
for i in string:
    if i == "," or i == "." or i == ";" or i == ":" or i == "?" or i == "!":
        res += 1

print(res)
