from bisect import bisect_left, bisect_right

N, M = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(N)]
LR = [[int(i) for i in input().split()] for _ in range(M)]

# 座圧
compressed = sorted([a for a, b in AB])
bomb = [0] * N
lr = []
for a, b in AB :
  a = bisect_left(compressed, a)
  bomb[a] = b
diff = [bomb[i-1] ^ bomb[i] for i in range(1, N)]
for l, r in LR :
  if compressed[-1] < l or r < compressed[0] : continue
  l = bisect_left(compressed, l)
  r = bisect_right(compressed, r) - 1
  if r < l : continue
  lr.append((l - 1, r))

# 最小全域木
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


print(bomb)
print(diff)
print(lr)