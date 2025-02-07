N = int(input())
A = [int(i) for i in input().split()]

ret = []
for a in A:
    if a % 2 == 0:
        ret.append(a)

print(*ret)
