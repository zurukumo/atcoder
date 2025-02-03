A, B, C, K = map(int, input().split())

if K % 2 == 0:
    ret = A - B
else:
    ret = B - A

if ret > 10**18:
    print("Unfair")
else:
    print(ret)
