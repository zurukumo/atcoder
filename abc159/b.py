S = input()

N = len(S)
A = S[:N//2]
B = S[N//2 + 1:]

if S == S[::-1] and A == A[::-1] and B == B[::-1] :
  print('Yes')
else :
  print('No')