import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
c = [int(i) for i in input().split()]
lr = [[int(i) - 1 for i in input().split()] for _ in range(Q)]

class BinaryIndexedTree() :
  def __init__(self, n) :
    self.n = n
    self.tree = [0] * (n + 1)
      
  def sum(self, i) :
    s = 0
    while i > 0 :
      s += self.tree[i]
      i -= i & -i
    return s
      
  def add(self, i, x) :
    while i <= self.n :
      self.tree[i] += x
      i += i & -i

BIT = BinaryIndexedTree(N + 5)
sch = [[i, l, r] for i, (l, r) in enumerate(lr)]
sch.sort(key=lambda x: x[2])
ret = [0] * Q
last = [-1] * (N + 1)

cur = 0
for i, l, r in sch :
  while cur <= r :
    BIT.add(cur + 1, 1)
    pos = last[c[cur]]
    if pos != -1 :
      BIT.add(pos + 1, -1)
    last[c[cur]] = cur
    cur += 1
  ret[i] = BIT.sum(r + 1) - BIT.sum(l)
for r in ret :
  print(r)