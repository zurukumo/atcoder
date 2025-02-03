from collections import defaultdict

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, K = map(int, input().split())
A = [int(i) for i in input().split()]

s = [0]

for i in range(N) :
    s.append((s[-1] + A[i]) % K)
    
for i in range(N + 1) :
    s[i] = (s[i] - i) % K

d = defaultdict(int)

ret = 0
for i in range(min(K, N + 1)) :
    ret += d[s[i]]
    d[s[i]] += 1
for i in range(K, N + 1) :
    d[s[i-K]] -= 1
    ret += d[s[i]]
    d[s[i]] += 1

print(ret)