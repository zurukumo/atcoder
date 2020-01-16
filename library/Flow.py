# Using DFS
class FordFulkerson :
  def __init__(self, N):
    self.N = N
    self.G = [[] for i in range(N)]

  def add_edge(self, fr, to, cap):
    self.G[fr].append([to, cap, len(G[to])])
    self.G[to].append([fr, 0, len(G[fr]) - 1])

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