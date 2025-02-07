X = int(input())

# 1111 → 1100 → 1200
Y = X - X % 100 + 100
print(Y - X)
