N, P = map(int, input().split())
a = [int(i) for i in input().split()]

ret = 0
for ai in a:
    if ai < P:
        ret += 1
print(ret)
