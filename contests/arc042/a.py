N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]

order = [[N - i, i + 1] for i in range(N)]
for i in range(M):
    order[a[i] - 1][0] = N + i

order.sort(reverse=True)
for i in range(N):
    print(order[i][1])
