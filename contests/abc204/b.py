N = int(input())
A = [int(i) for i in input().split()]

ret = 0
for a in A:
    if a > 10:
        ret += a - 10

print(ret)
