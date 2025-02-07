N = int(input())
S = input()

ret = 0
cnt = [0, 0]
for i, c in enumerate(S):
    c = int(c)
    if c == 0:
        cnt[0], cnt[1] = 1, cnt[0] + cnt[1]
    else:
        cnt[0], cnt[1] = cnt[1], cnt[0] + 1
    ret += cnt[1]

print(ret)
