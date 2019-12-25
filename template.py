import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
S = input()
N, K = map(int, input().split())
xy = [[int(i) for i in input().split()] for _ in range(N)]
x = [int(i) for i in input().split()]
S = [input() for _ in range(N)]
A = [int(input()) for _ in range(N)]