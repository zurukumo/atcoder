N = int(input())
B = [int(i) for i in input().split()]

# 添字が1から始まることに注意
class BinaryIndexedTree() :
  def __init__(self, N) :
    self.size = N
    self.tree = [0] * (N + 1)
      
  def sum(self, i) :
    s = 0
    while i > 0 :
      s += self.tree[i]
      i -= i & -i
    return s
      
  def add(self, i, x) :
    while i <= self.size :
      self.tree[i] += x
      i += i & -i
      
BIT = BinaryIndexedTree(N)

C = [[B[i], i + 1] for i in range(N)]
C.sort(reverse=True)

ret = 0
for i in range(N) :
  l = BIT.sum(C[i][1])
  r = i - l
  ret += min(l, r)
  BIT.add(C[i][1], 1)
  
print(ret)