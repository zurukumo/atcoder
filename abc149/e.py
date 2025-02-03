from bisect import bisect_left

N, M = map(int, input().split())
A = [int(i) for i in input().split()]

A.sort()

def calc(m) :
  c = 0
  for i in range(N) :
    c += N - bisect_left(A, m - A[i])
  return c

ng, ok = 0, A[-1] * 2 + 1
while ok - ng > 1 :
  m = (ok + ng) // 2

  if calc(m) <= M :
    ok = m
  else :
    ng = m
  
S = [A[0]]
for i in range(1, N) :
  S.append(S[-1] + A[i])
S.append(0)
S.append(0)

all = sum(A)
ret = 0
for i in range(N) :
  ret += all - S[bisect_left(A, ng - A[i])-1]
  ret += A[i] * (N - bisect_left(A, ng - A[i]))
ret -= (calc(ng) - M) * (ng)
print(ret)