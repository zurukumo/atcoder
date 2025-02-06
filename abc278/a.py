N, K = map(int, input().split())
A = [int(i) for i in input().split()]

for _ in range(K):
    A.pop(0)
    A.append(0)

print(*A)
