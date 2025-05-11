N, M = map(int, input().split())
A = [int(i) for i in input().split()]

cnt = [0] * (M + 1)
for a in A:
    cnt[a] += 1

ret = 0
while all(cnt[i] >= 1 for i in range(1, M + 1)):
    a = A.pop()
    cnt[a] -= 1
    ret += 1

print(ret)
