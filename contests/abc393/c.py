N, M = map(int, input().split())
uv = [[int(i) for i in input().split()] for _ in range(M)]

s = set()
for u, v in uv:
    u, v = max(u, v), min(u, v)
    if u != v:
        s.add((u, v))

print(M - len(s))
