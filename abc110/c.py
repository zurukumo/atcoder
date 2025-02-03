from collections import defaultdict

S = input()
T = input()

first_appear_s = dict()
first_appear_t = dict()

for i in range(len(S)):
    s = S[i]
    t = T[i]
    if not s in first_appear_s:
        first_appear_s[s] = i
    if not t in first_appear_t:
        first_appear_t[t] = i

    if first_appear_s[s] != first_appear_t[t]:
        print("No")
        break
else:
    print("Yes")
