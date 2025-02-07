A, L = map(int, input().split())
S = input()

ret = 0
now = 1
for s in S:
    if s == "+":
        now += 1
    else:
        now -= 1
    if now > L:
        ret += 1
        now = 1

print(ret)
