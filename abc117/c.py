N, M = map(int, input().split())
X = [int(i) for i in input().split()]

X.sort()

space = [X[i] - X[i - 1] for i in range(1, M)]
space.sort(reverse=True)
print(X[M - 1] - X[0] - sum(space[: N - 1]))
