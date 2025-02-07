N = int(input())
m = [int(i) for i in input().split()]

ret = 0
for i in range(N):
    if m[i] < 80:
        ret += 80 - m[i]

print(ret)
