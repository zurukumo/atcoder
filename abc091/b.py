from collections import Counter

N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]

print(max([0] + [v - t.count(k) for k, v in Counter(s).items()]))