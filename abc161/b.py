N, M = map(int, input().split())
A = [int(i) for i in input().split()]

ans = 0
s = sum(A)
for a in A:
    if a * (4 * M) >= s:
        ans += 1

if ans >= M:
    print('Yes')
else:
    print('No')
