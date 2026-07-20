import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
ABS = [input().split() for _ in range(N)]

ideal_change = 0
real_change = 0
for a, b, s in ABS:
    a, b = int(a), int(b)

    ideal_change += b - a
    if s == "take":
        real_change += b - a

print(ideal_change - real_change)
