N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]

revS = [s[::-1] for s in S]


def head_cnt(s):
    cnt = 0
    for c in s:
        if cnt < len(T) and c == T[cnt]:
            cnt += 1
    return cnt


def tail_cnt(s):
    cnt = 0
    for c in s[::-1]:
        if cnt < len(T) and c == T[len(T) - 1 - cnt]:
            cnt += 1
    return cnt


head = [0] * (len(T) + 1)
tail = [0] * (len(T) + 1)

for i in range(N):
    head[head_cnt(S[i])] += 1
    tail[tail_cnt(S[i])] += 1

for i in range(len(T) - 1, -1, -1):
    tail[i] += tail[i + 1]

ret = 0
for i in range(len(T) + 1):
    j = max(len(T) - i, 0)
    ret += head[i] * tail[j]

print(ret)
