N = int(input())
S = [input() for _ in range(N)]

dict = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
for s in S:
    if s[0] in "MARCH":
        dict[s[0]] += 1

counter = list(dict.values())
ret = 0
for i in range(len(counter)):
    for j in range(i + 1, len(counter)):
        for k in range(j + 1, len(counter)):
            ret += counter[i] * counter[j] * counter[k]
print(ret)
