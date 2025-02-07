N = int(input())
p = [int(i) for i in input().split()]

ret = 0
for i in range(0, N - 2):
    a, b, c = p[i : i + 3]
    if a < b < c or c < b < a:
        ret += 1

print(ret)
