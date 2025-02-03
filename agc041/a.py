N, M, V, P = map(int, input().split())
A = [int(i) for i in input().split()]

A.sort()

s = [A[0]]
for i in range(1, N) :
  s.append(A[i] + s[-1])

def check(m) :
  if m >= N - P :
    return True
  if A[m] + M < A[N - P] :
    return False

  rest = M * (V - P)
  x = A[m] + M
  for i in range(N - P + 1) :
    if i == m :
      continue
    rest -= min(x - A[i], M)
  return rest <= 0

ng, ok = -1, N
while ok - ng > 1 :
  m = (ok + ng) // 2
  if check(m) :
    ok = m
  else :
    ng = m

print(N - ng - 1)