import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, c = map(int, input().split())
print(a+b+c-max([a, b, c]))