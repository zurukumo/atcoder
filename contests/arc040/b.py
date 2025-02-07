N, R = map(int, input().split())
S = list(input())

while S and S[-1] == "o":
    S.pop()

ret = max(0, len(S) - R)
while True:
    while S and S[-1] == "o":
        S.pop()

    if len(S) == 0:
        break

    if len(S) <= R:
        ret += 1
        break
    else:
        ret += 1
        for _ in range(R):
            S.pop()

print(ret)
