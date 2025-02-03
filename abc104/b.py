S = input()


def check():
    if S[0] != "A" or S[2:-1].count("C") != 1:
        return "WA"

    ret = 0
    for s in S:
        if ord(s) < 97 or 122 < ord(s):
            ret += 1

    if ret != 2:
        return "WA"

    return "AC"


print(check())
