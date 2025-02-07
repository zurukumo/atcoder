import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N)]

AB.sort(key=lambda x: 2 * x[0] + x[1], reverse=True)

Asum = sum(a for a, _ in AB)
Bsum = 0
counter = 0
while Asum >= Bsum:
    a, b = AB[counter]
    Asum -= a
    Bsum += a + b
    counter += 1

print(counter)
