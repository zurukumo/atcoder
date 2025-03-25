N = int(input())
P = [int(i) for i in input().split()]
Q = [int(i) for i in input().split()]

pos = [0] * N
for i in range(N):
    pos[Q[i] - 1] = i

ret = []
for i in range(N):
    ret.append(Q[P[pos[i]] - 1])

print(*ret)
