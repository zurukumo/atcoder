K, M = map(int, input().split())
A = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

def matmul(x, y) :
  z = [[0] * K for _ in range(K)]
  for i in range(K) :
    for j in range(K) :
      for k in range(K) :
        z[i][j] ^= x[i][k] & y[k][j]
        
  return z
  
if M <= K :
  print(A[M-1])
  
else :
  M -= K
  x = [[0] * K for _ in range(K)]
  y = [[0] * K for _ in range(K)]
  
  x[0] = C
  for i in range(1, K) :
    x[i][i-1] = (1 << 40) - 1
  for i in range(K) :
    y[i][i] = (1 << 40) - 1
    
  while M :
    if M & 1 :
      y = matmul(y, x)
    x = matmul(x, x)
    M >>= 1
  
  ret = 0
  for i in range(K) :
    ret ^= y[0][i] & A[K-1-i]
    
  print(ret)