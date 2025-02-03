N, M = map(int, input().split())

ans = [[i, i + 2] for i in range(2, 4 * N + 2, 4)]

if M == 0:
    for row in ans:
        print(*row)
elif M < 0 or N == M or N == M + 1:
    print(-1)
else:
    ans[0][1] = ans[M + 1][0] + 1
    for row in ans:
        print(*row)
