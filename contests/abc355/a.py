A, B = map(int, input().split())

candidates = set([1, 2, 3])
candidates.remove(A)
if B in candidates:
    candidates.remove(B)

if len(candidates) == 1:
    print(candidates.pop())
else:
    print(-1)
