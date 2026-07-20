import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)


H, W = map(int, input().split())

if W * 100 * 100 >= 25 * H * H:
    print("Yes")
else:
    print("No")
