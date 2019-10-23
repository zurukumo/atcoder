class BinaryIndexedTree() :
    def __init__(self, N) :
        self.N = N
        self.tree = [0] * (N + 1)
        
    def sum(self, i) :
        s = 0
        while i > 0 :
            s += self.tree[i]
            i -= i & -i
        return s
        
    def add(self, i, x) :
        while i <= self.N :
            self.tree[i] += x
            i += i & -i