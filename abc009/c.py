from collections import Counter

N, K = map(int, input().split())
S = list(input())

T = sorted(S)
U = ''

same = 0
for i in range(N) :
  for j in range(N - i) :
    tmp = same
    if S[i] == T[j] :
      tmp += 1
    
    cnta = Counter(S[i+1:])
    cntb = Counter(T)
    cntb[T[j]] -= 1
    
    for k, v in cnta.items() :
      tmp += min(v, cntb[k])
      
    if N - tmp <= K :
      U += T[j]
      if S[i] == T[j] :
        same += 1
      T.pop(j)
      break
      
print(U)