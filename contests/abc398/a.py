N = int(input())

if N % 2 == 0:
    ret = "-" * (N // 2 - 1) + "==" + "-" * (N // 2 - 1)
else:
    ret = "-" * (N // 2) + "=" + "-" * (N // 2)

print(ret)
