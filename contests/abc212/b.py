X = [int(i) for i in input()]


def check(s):
    if s[0] == s[1] == s[2] == s[3]:
        return True

    if (s[1] - s[0]) % 10 == (s[2] - s[1]) % 10 == (s[3] - s[2]) % 10 == 1:
        return True

    return False


if check(X):
    print("Weak")
else:
    print("Strong")
