R, C, K = map(int, input().split())
N = int(input())

h = [0] * R
w = [0] * C
rc = []

for _ in range(N):
    r, c = map(int, input().split())
    h[r - 1] += 1
    w[c - 1] += 1
    rc.append((r - 1, c - 1))

ch = [0] * (N + 1)
cw = [0] * (N + 1)

for h_ in h:
    ch[h_] += 1
for w_ in w:
    cw[w_] += 1

ret = 0
for i in range(0, K + 1):
    ret += ch[i] * cw[K - i]

for r, c in rc:
    if h[r] + w[c] == K:
        ret -= 1
    elif h[r] + w[c] == K + 1:
        ret += 1

print(ret)
