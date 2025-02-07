N = int(input())

ret = []


def rec(n, i, ans):
    if n < 0:
        return

    if i == 0:
        if n % 2 == 0 and 0 <= n // 2 <= 9:
            ret.append(ans * 10 + n // 2)
        return

    j = n // (1 + 10**i)
    if 0 <= j <= 9:
        rec(n - (1 + 10**i) * j, i - 1, ans * 10 + j)
    if 0 <= j - 1 <= 9:
        rec(n - (1 + 10**i) * (j - 1), i - 1, ans * 10 + j - 1)


rec(N, 18, 0)

ret.sort()
print(len(ret))
for r in ret:
    print(r)
