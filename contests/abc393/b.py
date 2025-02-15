S = input()

ret = 0
for diff in range(1, len(S) + 10):
    for start in range(0, len(S) + 10):
        if S[start : start + 3 * diff : diff] == "ABC":
            ret += 1
print(ret)
