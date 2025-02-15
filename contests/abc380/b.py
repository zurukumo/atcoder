S = input()

print(*[len(bar) for bar in S.split("|")][1:-1])
