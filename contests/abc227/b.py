N = int(input())
S = [int(i) for i in input().split()]


def check(x):
    for a in range(1, 1001):
        for b in range(a, 1001):
            s = 4 * a * b + 3 * a + 3 * b
            if s > 1000:
                break
            if x == s:
                return True
    return False


ret = 0
for s in S:
    if not check(s):
        ret += 1


print(ret)
