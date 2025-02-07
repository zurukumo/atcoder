A, B, C = [int(input()) for _ in range(3)]

rank = sorted([A, B, C], reverse=True)

print(rank.index(A) + 1)
print(rank.index(B) + 1)
print(rank.index(C) + 1)
