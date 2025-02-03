N = int(input())


def hash(S):
    ret = 0
    for s in S:
        ret *= 26
        ret += ord(s) - 97
    return ret


s = [hash(sorted(input())) for _ in range(N)]

s.sort()
s.append(-1)

count = 1
ret = 0
for i in range(1, N + 1):
    if s[i] == s[i - 1]:
        count += 1
    else:
        if count >= 2:
            ret += count * (count - 1) // 2
        count = 1

print(ret)
