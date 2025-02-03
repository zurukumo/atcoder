N, K = map(int, input().split())

dp2 = [0] * (2 * N + 1)
for n in range(2, 2 * N + 1):
    l = max(1, n - N)
    r = min(N, n - 1)
    dp2[n] = r - l + 1

sdp2 = dp2[::]
for n in range(1, 2 * N + 1):
    sdp2[n] += sdp2[n - 1]

dp3 = [0] * (3 * N + 1)
for n in range(3, 3 * N + 1):
    l = max(1, n - 2 * N)
    r = min(N, n - 2)
    dp3[n] = sdp2[n - l] - sdp2[n - r - 1]

sdp3 = dp3[::]
for n in range(1, 3 * N + 1):
    sdp3[n] += sdp3[n - 1]
    if sdp3[n] >= K:
        break
K -= sdp3[n - 1]

for a in range(1, N + 1):
    if 2 <= n - a <= 2 * N:
        if K > dp2[n - a]:
            K -= dp2[n - a]
        else:
            break

for b in range(1, N + 1):
    c = n - a - b
    if 1 <= c <= N:
        K -= 1
    if K == 0:
        print(a, b, c)
        break
