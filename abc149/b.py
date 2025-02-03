A, B, K = map(int, input().split())

if K >= A :
  K -= A
  A = 0
  B = max(0, B - K)
  
else :
  A -= K
  
print(A, B)