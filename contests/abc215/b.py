import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

i = 0
while 2 ** (i + 1) <= N:
    i += 1
print(i)
