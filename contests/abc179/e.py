N, X, M = map(int, input().split())

done = [False] * (M + 1)
a = []

done[X] = True
a.append(X)

x = X * X % M
while not done[x]:
    done[x] = True
    a.append(x)
    x = x * x % M

ret = 0
for i, ai in enumerate(a):
    if ai == x or N == 0:
        break
    ret += ai
    N -= 1

loop_s = sum(a[i:])
loop_l = len(a) - i

ret += loop_s * (N // loop_l)
N %= loop_l

for aj in a[i:]:
    if N == 0:
        break
    ret += aj
    N -= 1

print(ret)
