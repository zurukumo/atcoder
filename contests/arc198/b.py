import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())
    if Y % 2 == 1 and Z == 0:
        print("No")
        continue
    if X * 2 >= Y and X >= Z:
        print("Yes")
    else:
        print("No")
