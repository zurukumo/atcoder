N = int(input())
A = [int(input()) for _ in range(N)]

ret = 0
for i in range(N):
    if A[i] > 2:
        x = (A[i] - 1) // 2
        ret += x
        A[i] -= x * 2

for i in range(N - 1):
    if A[i] == 2:
        ret += 1
    elif A[i] == 1 and A[i + 1] >= 1:
        ret += 1
        A[i + 1] -= 1

if A[-1] == 2:
    ret += 1

print(ret)
