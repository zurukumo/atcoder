n = int(input())
p = [int(i) for i in input().split()]

if (p[1] - p[0]) % n == 1:
    ret = min(-p[-1] % n, p[-1] % n + 2)
else:
    ret = min(p[0] % n + 1, -p[0] % n + 1)
print(ret)
