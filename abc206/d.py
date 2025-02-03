from bisect import bisect_left

N = int(input())
A = [int(i) for i in input().split()]

s = sorted(list(set(A)))
B = [bisect_left(s, A[i]) for i in range(N)]

class UnionFind :
  def __init__(self, N) :
    self.parent = [-1] * N
      
  def root(self, x) :
    while self.parent[x] >= 0:
      x = self.parent[x]
    return x

  def unite(self, x, y) :
    rx = self.root(x)
    ry = self.root(y)

    if rx != ry :
      if self.parent[rx] > self.parent[ry] :
        self.parent[rx] = ry
      else :
        if self.parent[rx] == self.parent[ry] :
          self.parent[rx] -= 1
        self.parent[ry] = rx

  def same(self, x, y) :
    return self.root(x) == self.root(y)
      
  def size(self, x) :
    return -self.parent[self.root(x)]
    
UF = UnionFind(len(s))
for i in range((N + 1) // 2):
    UF.unite(B[i], B[N-1-i])

ret = len(s)
for p in UF.parent:
  if p < 0:
    ret -= 1

print(ret)