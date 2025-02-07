H, W = map(int, input().split())
S = [input() for _ in range(H)]

print(sum(row.count("#") for row in S))
