N, K = map(int, input().split())
S = input() + "."

count = []
pre = S[0]
c = 1
for t in S[1:]:
    if t == pre:
        c += 1
    else:
        count.append(c)
        pre = t
        c = 1

ret = sum(count) - len(count)
if K < len(count) // 2:
    ret += 2 * K
else:
    ret = N - 1
print(ret)
