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
      
class WeightedUnionFind :
  def __init__(self, N) :
    self.parent = [-1] * N
    self.potential = [0] * N
    
  def root(self, x) :
    while self.parent[x] >= 0:
      x = self.parent[x]
    return x

  def unite(self, x, y, w) :
    rx = self.root(x)
    ry = self.root(y)
    
    if rx != ry :
      w = w + self.weight(x) - self.weight(y)
      if self.parent[rx] > self.parent[ry] :
        self.parent[rx] = ry
        self.potential[rx] = -w
      else :
        if self.parent[rx] == self.parent[ry] :
          self.parent[rx] -= 1
        self.parent[ry] = rx
        self.potential[ry] = w

  def same(self, x, y) :
    return self.root(x) == self.root(y)
      
  def size(self, x) :
    return -self.parent[self.root(x)]
  
  def weight(self, x) :
    w = 0
    while self.parent[x] >= 0 :
      w += self.potential[x]
      x = self.parent[x]
    return w
    
  def diff(self, x, y) :
    return self.weight(y) - self.weight(x)