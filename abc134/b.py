from math import ceil

N, D = map(int, input().split())
print(ceil(N / (D + D + 1)))
