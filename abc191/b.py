N, X = map(int, input().split())
A = [int(i) for i in input().split()]

B = []
for a in A:
    if a == X:
        continue
    B.append(a)

print(*B)
