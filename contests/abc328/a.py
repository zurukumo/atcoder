N, X = map(int, input().split())
S = [int(i) for i in input().split()]

print(sum(s if s <= X else 0 for s in S))
