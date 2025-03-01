N = int(input())
P = [int(i) for i in input().split()]
S = input()

mod = 998244353

ret = 0
first = P[0] - 1

# 最初をLにする
if S[first] == "L" or S[first] == "?":
    tmp = 1
    done = [False] * N
    for p in P:
        i = p - 1
        j = (i + 1) % N
        if done[i]:
            break

        if done[j]:
            if S[i] == "?":
                tmp *= 2
                tmp %= mod
            done[i] = True
        elif not done[j]:
            if S[i] == "R":
                break
            done[i] = True
    else:
        ret += tmp
        ret %= mod

# 最初をRにする
if S[first] == "R" or S[first] == "?":
    tmp = 1
    done = [False] * N
    for p in P:
        i = p - 1
        j = (i + 1) % N
        if done[j]:
            break

        if done[i]:
            if S[i] == "?":
                tmp *= 2
                tmp %= mod
            done[j] = True
        elif not done[i]:
            if S[i] == "L":
                break
            done[j] = True
    else:
        ret += tmp
        ret %= mod

print(ret)
