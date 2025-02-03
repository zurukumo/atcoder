import sortedcontainers

N, M, K = map(int, input().split())
A = [int(i) for i in input().split()]


class Queue:
    def __init__(self, K):
        self.lqueue = sortedcontainers.SortedList()
        self.rqueue = sortedcontainers.SortedList()
        self.s = 0
        self.K = K

    def add(self, a):
        self.lqueue.add(a)
        self.s += a

    def remove(self, a):
        if a in self.lqueue:
            self.lqueue.remove(a)
            self.s -= a
        else:
            self.rqueue.remove(a)

    def balance(self):
        while len(self.lqueue) > self.K:
            v = self.lqueue.pop()
            self.rqueue.add(v)
            self.s -= v
        while len(self.lqueue) < self.K and self.rqueue:
            v = self.rqueue.pop(0)
            self.lqueue.add(v)
            self.s += v
        while self.lqueue and self.rqueue and self.lqueue[-1] > self.rqueue[0]:
            lv = self.lqueue.pop()
            rv = self.rqueue.pop(0)
            self.lqueue.add(rv)
            self.rqueue.add(lv)
            self.s += rv - lv


queue = Queue(K)
ret = []
for i in range(N):
    queue.add(A[i])
    if i >= M:
        queue.remove(A[i - M])
    queue.balance()
    if i >= M - 1:
        ret.append(queue.s)


print(*ret)
