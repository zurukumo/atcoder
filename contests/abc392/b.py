N, M = map(int, input().split())
A = [int(i) for i in input().split()]

s = set(range(1, N + 1)) - set(A)
print(len(s))
print(*s)
