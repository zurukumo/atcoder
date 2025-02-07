N = int(input())

ret = float("inf")
for i in range(6):
    ret = min(ret, 100 * i + max(0, N - 10 * i) * 15)
print(ret)
