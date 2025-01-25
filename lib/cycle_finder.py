# 辺が高々一つの閉路に含まれる場合のみ有効
# たとえば1->2, 1->3, 2->4, 3->4, 4->1のグラフでは使えない
class CycleFinder:
    def __init__(self, n, graph):
        self.n = n
        self.graph = graph
        self.seen = [False] * n
        self.finished = [False] * n
        self.group = 0
        self.groups = [-1] * n
        self.history = []

    def __dfs(self, pre, cur, is_prohibited_reverse=True):
        self.seen[cur] = True
        self.groups[cur] = self.group
        self.history.append(cur)

        for nex in self.graph[cur]:
            if is_prohibited_reverse and pre == nex:
                continue

            if self.finished[nex]:
                continue

            if self.groups[nex] != -1 and self.groups[nex] != self.group:
                continue

            if self.seen[nex] and not self.finished[nex]:
                return nex

            pos = self.__dfs(cur, nex, is_prohibited_reverse)
            if pos != -1:
                return pos

        self.finished[cur] = True
        self.history.pop()
        return -1

    def __reconstruct(self, pos):
        cycle = []
        while self.history:
            cur = self.history.pop()
            cycle.append(cur)
            if cur == pos:
                break

        return cycle

    def detect(self, is_prohibited_reverse=True):
        cycles = []
        for cur in range(self.n):
            if self.seen[cur]:
                continue
            self.history = []
            pos = self.__dfs(-1, cur, is_prohibited_reverse)
            if pos != -1:
                cycles.append(self.__reconstruct(pos))
            self.group += 1
        return cycles
