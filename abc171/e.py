import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
a = [int(i) for i in input().split()]

b = []
for i in range(N - 1) :
  b.append(a[i] ^ a[(i + 1) % N])

x = 0
for i in range(0, N - 1, 2) :
  x ^= b[i]

ret = [a[-1] ^ x]
for c in b[::-1] :
  ret.append(c ^ ret[-1])

ret = ret[::-1]
print(*ret)