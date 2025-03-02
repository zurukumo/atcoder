N, R = map(int, input().split())
DA = [[int(i) for i in input().split()] for _ in range(N)]

for d, a in DA:
    if d == 1 and 1600 <= R <= 2799:
        R += a
    if d == 2 and 1200 <= R <= 2399:
        R += a

print(R)
