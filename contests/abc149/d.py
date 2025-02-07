N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()


def score(c):
    if c == "r":
        return P
    if c == "s":
        return R
    if c == "p":
        return S


ret = 0
for fr in range(K):
    U = list(T[fr::K])
    s = 0
    s += score(U[0])
    for i in range(1, len(U)):
        if U[i] == U[i - 1]:
            U[i] = "#"
        else:
            s += score(U[i])
    ret += s

print(ret)
