import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
A = [int(i) for i in input().split()]

A2 = [(a, i) for i, a in enumerate(A)]
A2.sort(key=lambda x: x[0])

A3 = [
    (original_a, compressed_a + 1, original_index)
    for compressed_a, (original_a, original_index) in enumerate(A2)
]
A3.sort(key=lambda x: x[2], reverse=True)


class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.n:
            self.tree[i] += x
            i += i & -i


total_bit = BinaryIndexedTree(N)
count_bit = BinaryIndexedTree(N)
ans = 0
for oa, ca, _ in A3:
    total = total_bit.sum(N) - total_bit.sum(ca)
    count = count_bit.sum(N) - count_bit.sum(ca)
    ans += total - count * oa
    total_bit.add(ca, oa)
    count_bit.add(ca, 1)

print(ans)
