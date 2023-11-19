spring = [1, 2, 3]
summer = [4, 5, 6]
autumn = [7, 8, 9]
winter = [10, 11, 12]

month = int(input())

if month in spring:
    print("spring")
elif month in summer:
    print("summer")
elif month in autumn:
    print("autumn")
else:
    print("winter")
