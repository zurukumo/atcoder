N = int(input())
S = input()
T = input()


def same(s, t):
    if s == t or (s in "1l" and t in "1l") or (s in "0o" and t in "0o"):
        return True
    return False


if all(same(s, t) for s, t in zip(S, T)):
    print("Yes")
else:
    print("No")
