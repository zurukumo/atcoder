import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

diff = 0
cura = 0
curb = 0
for i, a in enumerate(A[:-1]):
    nexa = (A[i] + A[i + 1] - cura) % 2
    nexb = (B[i] - curb) % 2
    if nexa != nexb:
        diff += 1
    cura = nexa
    curb = nexb

print(min(diff, 1 + (N - 1 - diff)))
