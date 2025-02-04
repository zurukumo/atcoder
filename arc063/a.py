S = input()

ret = 0
for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        ret += 1

print(ret)
