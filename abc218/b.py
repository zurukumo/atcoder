P = [int(i) for i in input().split()]

ret = ''
for p in P:
    ret += chr(ord('a') + p - 1)

print(ret)
