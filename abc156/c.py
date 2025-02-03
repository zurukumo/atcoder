N = int(input())
X = [int(i) for i in input().split()]

ret = float("inf")
for i in range(0, 101):
    s = 0
    for j in range(N):
        s += (X[j] - i) ** 2
    ret = min(ret, s)

print(ret)
