H = int(input())

cnt = 1
ret = 0
while H >= 1:
    H //= 2
    ret += cnt
    cnt *= 2

print(ret)
