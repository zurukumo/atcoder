A, B, K = map(int, input().split())

ret = []
for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        ret.append(i)
print(ret[-K])
