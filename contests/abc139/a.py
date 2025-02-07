S = input()
T = input()

ret = 0
for i in range(3):
    if S[i] == T[i]:
        ret += 1
print(ret)
