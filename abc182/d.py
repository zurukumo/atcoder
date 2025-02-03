N = int(input())
A = [int(i) for i in input().split()]

s = [0] + A[::]
for i in range(1, N + 1) :
  s[i] += s[i - 1]

t = s[::]
for i in range(1, N + 1) :
  t[i] += t[i - 1]

m = s[::]
for i in range(1, N + 1) :
  m[i] = max(m[i], m[i - 1])


ret = 0
for i in range(1, N + 1) :
  ret = max(ret, t[i - 1] + m[i])
ret = max(ret, t[-1])

print(ret)