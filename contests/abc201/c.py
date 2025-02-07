S = input()

ret = 0
for i in range(10000):
    i = "0000" + str(i)
    c = [int(i[-1]), int(i[-2]), int(i[-3]), int(i[-4])]

    for j in range(10):
        if S[j] == "o" and j not in c:
            break

        if S[j] == "x" and j in c:
            break

    else:
        ret += 1

print(ret)
