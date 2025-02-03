A, B, C = map(int, input().split())
if A == B == C and A % 2 == 0:
    print(-1)
else:
    ret = 0
    while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        A, B, C = B // 2 + C // 2, C // 2 + A // 2, A // 2 + B // 2
        ret += 1

    print(ret)
