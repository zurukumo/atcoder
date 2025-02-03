N = int(input())

ret = []
s = [str(i) for i in range(1, 7)]
for i in range(30) :
  s[i % 5], s[i % 5 + 1] = s[i % 5 + 1], s[i % 5]
  ret.append(''.join(s))

print(ret[(N - 1) % 30])