N = int(input())
a = [int(i) + 1 for i in input().split()]

# 1-indexed
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
      
BIT = BinaryIndexedTree(3 * (10 ** 5) + 10)
ret = 0
for i, p in enumerate(a) :
  BIT.add(p, 1)
  ret += i + 1 - BIT.sum(p)

for i in range(N) :
  print(ret)
  ret -= BIT.sum(a[i])
  ret += N - BIT.sum(a[i] - 1)