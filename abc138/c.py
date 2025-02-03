import sys

input = sys.stdin.readline

N = int(input())
v = [int(i) for i in input().split()]

v.sort()
s = v[0]
for i in range(1, N):
    s = (s + v[i]) / 2

print(s)
