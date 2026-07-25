import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
X = [int(i) for i in input().split()]

if all(x < 0 for x in X):
    print("Yes")
else:
    print("No")
