N, G, E = map(int, input().split())
p = [int(i) for i in input().split()]
ab = [[int(i) for i in input().split()] for _ in range(E)]

class FordFulkerson:
  def __init__(self, N):
    self.N = N
    self.G = [[] for i in range(N)]

  def add_edge(self, fr, to, cap):
    self.G[fr].append([to, cap, len(self.G[to])])
    self.G[to].append([fr, 0, len(self.G[fr]) - 1])

  def dfs(self, cur, t, f):
    if cur == t:
      return f
      
    self.used[cur] = True
    for i, (nex, cap, rev) in enumerate(self.G[cur]) :
      if cap > 0 and not self.used[nex] :
        d = self.dfs(nex, t, min(f, cap))
        if d:
          self.G[cur][i][1] -= d
          self.G[nex][rev][1] += d
          return d
    return 0

  def flow(self, s, t):
    flow = 0
    f = INF = 10**9 + 7
    N = self.N
    while f:
        self.used = [False] * N
        f = self.dfs(s, t, INF)
        flow += f
    return flow
    
FF = FordFulkerson(N + 1)
for a, b in ab :
  FF.add_edge(a, b, 1)
  FF.add_edge(b, a, 1)
for i in range(G) :
  FF.add_edge(p[i], N, 1)
  
print(FF.flow(0, N))