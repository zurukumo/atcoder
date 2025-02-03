N = int(input())
S = [ord(i) - 97 for i in input()]
Q = int(input())

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
      
alph = [BinaryIndexedTree(N + 10) for _ in range(26)]
for i in range(N) :
  alph[S[i]].add(i + 1, 1)

for _ in range(Q) :
  type, x, y = input().split()
  if type == '1' :
    x = int(x)
    s = S[x - 1]
    alph[s].add(x, -1)
    alph[ord(y) - 97].add(x, 1)
    S[x - 1] = ord(y) - 97
  else :
    x, y = int(x), int(y)
    ret = 0
    for i in range(26) :
      if alph[i].sum(y) - alph[i].sum(x - 1) > 0 :
        ret += 1
    print(ret)