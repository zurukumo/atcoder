N = int(input())

ret = float("inf")
for b in range(61):
    a = N // 2**b
    c = N - a * 2**b
    ret = min(ret, a + b + c)

print(ret)
