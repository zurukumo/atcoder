import sys
from math import gcd

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())
NSK = [[int(i) for i in input().split()] for _ in range(T)]


for n, s, k in NSK:
    div = gcd(n, s, k)
    n //= div
    s //= div
    k //= div

    if gcd(n, k) != 1:
        print(-1)
    else:
        print(pow(k, -1, n) * (-s) % n)
