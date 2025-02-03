N = int(input())
S = input()

ret = []
s = 0
for i, c in enumerate(S):
    s += (i + 1) * int(c)
    ret.append(s)

for i in range(len(ret) - 1, 0, -1):
    ret[i - 1] += ret[i] // 10
    ret[i] %= 10

print("".join(map(str, ret)))
