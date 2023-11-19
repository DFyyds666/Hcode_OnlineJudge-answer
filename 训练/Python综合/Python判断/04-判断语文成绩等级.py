score = int(input())

if score >= 90:
    print("excellent")
elif score >= 80:
    print("good")
elif score >= 60:
    print("pass")
else:
    print("failed")

if score + 5 >= 90:
    print("yes")
else:
    print("no")
