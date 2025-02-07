S = list(input())
T = list(input())


def check(S, T):
    for _ in range(len(S)):
        if S == T:
            return "Yes"
        else:
            t = T.pop()
            T = [t] + T
    return "No"


print(check(S, T))
