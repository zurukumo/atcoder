N, M = map(int, input().split())
C = [int(i) for i in input().split()]
KA = [[int(i) for i in input().split()] for _ in range(M)]

ret = float("inf")

animals_by_zoo = [[] for _ in range(N)]

for zoo, ka in enumerate(KA):
    animals = ka[1:]
    for animal in animals:
        animals_by_zoo[animal - 1].append(zoo)

for i in range(3**N):
    cost = 0
    animals = [0] * M
    for j in range(N):
        cnt = i % 3
        i //= 3
        for animal in animals_by_zoo[j]:
            animals[animal] += cnt
        cost += C[j] * cnt

    if all(a >= 2 for a in animals):
        ret = min(ret, cost)

print(ret)
