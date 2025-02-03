N = int(input())
S = [input() for _ in range(N)]

ret = 0
seen = set()
for s in S:
    if s in seen or s[::-1] in seen:
        continue

    seen.add(s)
    ret += 1

print(ret)
