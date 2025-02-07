N, M = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(M)]

vec = [[] for _ in range(N)]
for A, B in AB:
    vec[A - 1].append(B - 1)

ret = 0
for i in range(N):
    visited = [False] * N
    q = [i]
    c = 1
    visited[i] = True
    while q:
        cur = q.pop()
        for nex in vec[cur]:
            if visited[nex]:
                continue

            q.append(nex)
            visited[nex] = True
            c += 1

    ret += c

print(ret)
