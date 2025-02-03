N, M = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(M)]
K = int(input())
CD = [[int(i) for i in input().split()] for _ in range(K)]

ret = 0
for mask in range(1 << K) :
  tmp = 0
  sara = [0] * (N + 1)
  for C, D in CD :
    if mask & 1 :
      sara[C] = 1
    else :
      sara[D] = 1
    mask >>= 1
  
  for A, B in AB :
    if sara[A] and sara[B] :
      tmp += 1
      
  ret = max(ret, tmp)
  
print(ret)