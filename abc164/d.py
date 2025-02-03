from collections import Counter

S = input()

x = [0]
dec = 1
for s in S[::-1] :
  x.append((x[-1] + dec * int(s)) % 2019)
  dec *= 10
  dec %= 2019

ret = 0
for v in Counter(x).values() :
  ret += v * (v - 1) // 2
print(ret)