n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]

ret = float("inf")
for i in range(1, 11):
    for j in range(1, 11):
        if i == j:
            continue

        s = 0
        for k, v in enumerate(a):
            if k % 2 == 0 and v != i:
                s += c
            elif k % 2 == 1 and v != j:
                s += c

        ret = min(ret, s)

print(ret)
