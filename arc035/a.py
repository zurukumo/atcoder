s = input()
n = len(s)

for i in range(n) :
  if s[i] != s[n-1-i] and s[i] != '*' and s[n-1-i] != '*' :
    print('NO')
    break
else :
  print('YES')