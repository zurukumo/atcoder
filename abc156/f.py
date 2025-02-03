k, q = map(int, input().split())
d = [int(i) for i in input().split()]
nxm = [[int(i) for i in input().split()] for _ in range(q)]

for n, x, m in nxm :
  an = x
  for i in range(k) :
    if d[i] % m != 0 :
      an += ((n - i - 2) // k + 1) * (d[i] % m)
    else :
      an += ((n - i - 2) // k + 1) * m
  print(n - 1 - (an // m - x // m))