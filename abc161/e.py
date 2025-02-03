from heapq import heappush, heappop

N, K, C = map(int, input().split())
S = input()

if C == 0 :
  if K == S.count('o') :
    for i, s in enumerate(S) :
      if s == 'o' :
        print(i + 1)

else :
  N += 2
  S = 'x' + S + 'x'

  dpL = [0] * N
  dpR = [0] * N
  for l in range(1, N) :
    r = N - 1 - l
    dpL[l] = max(dpL[l - 1], int(S[l] == 'o'))
    dpR[r] = max(dpR[r + 1], int(S[r] == 'o'))
    if l - C - 1 >= 0 and S[l] == 'o' :
      dpL[l] = max(dpL[l], dpL[l - C - 1] + 1)
    if r + C + 1 < N and S[r] == 'o' :
      dpR[r] = max(dpR[r], dpR[r + C + 1] + 1)

  h = []
  for r in range(C + 1) :
    heappush(h, (-dpR[r], r))

  for l in range(1, N) :
    r = l - 1 + C + 1
    if r < N :
      cost = dpL[l - 1] + dpR[r]
    else :
      cost = dpL[l - 1]
    heappush(h, (-cost, r))
    while h[0][1] <= l :
      heappop(h)
    
    if -h[0][0] < K and S[l] == 'o' :
      print(l)