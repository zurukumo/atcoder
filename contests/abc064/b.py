import sys

input = sys.stdin.readline

N = int(input())
a = [int(i) for i in input().split()]

print(max(a) - min(a))
