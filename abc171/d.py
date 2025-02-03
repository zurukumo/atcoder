import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]
Q = int(input())
BC = [[int(i) for i in input().split()] for _ in range(Q)]

cnt = Counter(A)
ret = sum(A)
for B, C in BC :
  ret = ret + cnt[B] * (C - B)
  cnt[C] += cnt[B]
  cnt[B] = 0
  print(ret)