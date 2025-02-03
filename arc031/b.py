S = input()
N = len(S)

for i in range(N) :
  if S[i] != S[N-1-i] :
    print('NO')
    break
else :
  print('YES')