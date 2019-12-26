class DoublingLowestCommonAncestor :
  def __init__(self, G) :
    N = len(G)
    K = len(bin(N)) - 1
    
    # bfs
    par = [[-1] * N for i in range(K)]
    rnk = [-1] * N
    rnk[0] = 0
    
    q = [(0, -1)]
    while q :
      cur, pre = q.pop()
      for nex in G[cur] :
        if nex != pre :
          par[0][nex] = cur
          q.append((nex, cur))
          rnk[nex] = rnk[cur] + 1
    
    # doubling
    for i in range(1, K) :
      for j in range(N) :
        if par[i-1][j] > 0 :
          par[i][j] = par[i-1][par[i-1][j]]
    
    self.K = K
    self.par = par
    self.rnk = rnk    
    
  def query(self, a, b) :
    if self.rnk[a] > self.rnk[b] :
      a, b = b, a

    diff = self.rnk[b] - self.rnk[a]
    for i in range(self.K - 1, -1, -1) :
      if diff & (1 << i) :
        b = self.par[i][b]
    
    if a == b :
      return a
    
    for i in range(self.K - 1, -1, -1) :
      if self.par[i][a] != self.par[i][b] :
        a, b = self.par[i][a], self.par[i][b]

    return self.par[0][a]