Y = int(input())

if Y % 4 != 0:
    ret = 365
elif Y % 4 == 0 and Y % 100 != 0:
    ret = 366
elif Y % 100 == 0 and Y % 400 != 0:
    ret = 365
elif Y % 400 == 0:
    ret = 366

print(ret)
