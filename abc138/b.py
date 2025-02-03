import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
A = [int(i) for i in input().split()]

bunbo = 0
for a in A:
    bunbo += 1 / a

print(1 / bunbo)
