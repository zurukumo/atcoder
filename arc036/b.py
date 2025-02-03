import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
h = [int(input()) for _ in range(N)]

dpl = [1] * N
dpr = [1] * N
for i in range(1, N) :
    if h[i] > h[i-1] :
        dpl[i] = dpl[i-1] + 1
    if h[N-1-i] > h[N-i] :
        dpr[N-1-i] = dpr[N-i] + 1

print(max([dpl[i] + dpr[i] for i in range(N)]) - 1)
    