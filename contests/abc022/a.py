N, S, T = map(int, input().split())
W = int(input())
A = [0] + [int(input()) for _ in range(N - 1)]

ret = 0

for a in A:
    W += a
    if S <= W <= T:
        ret += 1

print(ret)
