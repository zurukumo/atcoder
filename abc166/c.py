N, M = map(int, input().split())
H = [int(i) for i in input().split()]
vec = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    vec[A - 1].append(B - 1)
    vec[B - 1].append(A - 1)

ret = 0
for i in range(N):
    for j in vec[i]:
        if H[j] >= H[i]:
            break
    else:
        ret += 1

print(ret)
