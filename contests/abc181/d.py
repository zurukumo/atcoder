from collections import Counter

S = input()


def judge():
    if len(S) == 1:
        if int(S) % 8 == 0:
            return "Yes"
        else:
            return "No"

    if len(S) == 2:
        a = int(S[0]) * 10 + int(S[1])
        b = int(S[1]) * 10 + int(S[0])
        if a % 8 == 0 or b % 8 == 0:
            return "Yes"
        else:
            return "No"

    cnt = Counter(S)

    for i in range(8, 1000, 8):
        s = "{:03d}".format(i)
        for j in range(0, 10):
            if cnt[str(j)] < s.count(str(j)):
                break
        else:
            return "Yes"

    return "No"


print(judge())
