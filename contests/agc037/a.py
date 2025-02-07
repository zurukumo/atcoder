S = input()

ret = 1
pre = S[0]
flag = True
i = 1
while i < len(S):
    if flag and S[i] == pre:
        if i == len(S) - 1:
            break
        flag = False
        i += 2
    else:
        flag = True
        pre = S[i]
        i += 1
    ret += 1

print(ret)
