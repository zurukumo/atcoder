N = int(input())
S = input()

S += "XYZ"

cnt = S.count("ARC")
pre3 = [None, 0]
pre2 = [None, 0]
pre1 = [None, 0]
ret = 0
for i, c in enumerate(S):
    if c != pre1[0]:
        if pre3[0] == "A" and pre2[0] == "R" and pre2[1] == 1 and pre1[0] == "C":
            ret += min(pre3[1], pre1[1])
        pre3 = pre2
        pre2 = pre1
        pre1 = [c, 1]
    else:
        pre1[1] += 1

print(min(2 * cnt, ret))
