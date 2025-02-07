from collections import Counter

S = input()

c = Counter(S)

one = 0
two = 0

for i in c.values():
    one += i % 2
    two += i // 2

if one == 0:
    print(two * 2)
else:
    print((two // one) * 2 + 1)
