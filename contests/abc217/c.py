import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
p = [int(i) for i in input().split()]

ret = [0] * N

for i in range(N):
    ret[p[i] - 1] = i + 1

print(*ret)
