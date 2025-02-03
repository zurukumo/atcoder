Q = int(input())
TX = [[int(i) for i in input().split()] for _ in range(Q)]

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
            
BIT = BinaryIndexedTree(200000)
for t, x in TX :
    if t == 1 :
        BIT.add(x, 1)
    else :
        ng, ok = -1, 200000
        while ok - ng > 1 :
            m = (ng + ok) // 2
            if BIT.sum(m) < x :
                ng = m
            else :
                ok = m
        print(ok)
        BIT.add(ok, -1)