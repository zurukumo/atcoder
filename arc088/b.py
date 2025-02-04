s = input() + "."

count = []
pre = s[0]
c = 1
for t in s[1:]:
    if t == pre:
        c += 1
    else:
        count.append(c)
        pre = t
        c = 1

m = float("inf")
tot = sum(count)
now = 0
for c in count:
    now += c
    m = min(m, max(now, tot - now))
print(m)
