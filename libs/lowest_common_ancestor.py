class DoublingLowestCommonAncestor:
    def __init__(self, G):
        N = len(G)
        K = len(bin(N)) - 1

        # bfs
        parent = [[-1] * N for _ in range(K)]
        rank = [-1] * N
        rank[0] = 0

        q = [(0, -1)]
        while q:
            cur, pre = q.pop()
            for nex in G[cur]:
                if nex != pre:
                    parent[0][nex] = cur
                    q.append((nex, cur))
                    rank[nex] = rank[cur] + 1

        # doubling
        for i in range(1, K):
            for j in range(N):
                if parent[i - 1][j] != -1:
                    parent[i][j] = parent[i - 1][parent[i - 1][j]]

        self.K = K
        self.parent = parent
        self.rank = rank

    def query(self, a, b):
        if self.rank[a] > self.rank[b]:
            a, b = b, a

        diff = self.rank[b] - self.rank[a]
        for i in range(self.K - 1, -1, -1):
            if diff & (1 << i):
                b = self.parent[i][b]

        if a == b:
            return a

        for i in range(self.K - 1, -1, -1):
            if self.parent[i][a] != self.parent[i][b]:
                a, b = self.parent[i][a], self.parent[i][b]

        return self.parent[0][a]
