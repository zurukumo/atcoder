N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]

T.sort()

ret = 1
cnt = 1
pre = T[0]
for i in range(1, N):
    if cnt == C or T[i] > pre + K:
        ret += 1
        cnt = 1
        pre = T[i]

    else:
        cnt += 1

print(ret)
