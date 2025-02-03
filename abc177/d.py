N, M = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(M)]

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
    
UF = UnionFind(N)
for A, B in AB :
  A -= 1
  B -= 1
  UF.unite(A, B)
  
c = [0] * N
for i in range(N) :
  c[UF.root(i)] += 1
print(max(c))