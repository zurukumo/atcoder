N, A, B = map(int, input().split())

if A % 2 == B % 2:
    ret = abs(B - A) // 2

else:
    ret = min((A - 1 + B - 1 - 1) // 2, (N - A + N - B - 1) // 2) + 1

print(ret)
