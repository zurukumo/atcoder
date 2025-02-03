A, B = map(int, input().split())

if A > B:
    A, B = B, A

ret = 0
while A != B:
    if B - A > 7:
        A += 10
        ret += 1
    elif B - A > 3:
        A += 5
        ret += 1
    else:
        A += 1
        ret += 1

    A, B = min(A, B), max(A, B)

print(ret)
