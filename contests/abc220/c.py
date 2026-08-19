import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
A = [int(i) for i in input().split()]
X = int(input())

ret = 0

s = sum(A)
ret += X // s * N
X %= s

A.reverse()
while X >= 0:
    X -= A.pop()
    ret += 1

print(ret)
