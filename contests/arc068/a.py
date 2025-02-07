x = int(input())

ret = (x // 11) * 2
if 1 <= x % 11 <= 6:
    ret += 1
elif 6 < x % 11:
    ret += 2

print(ret)
