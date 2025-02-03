N, M, T = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(M)]

def judge():
  t = 0
  r = N
  for A, B in AB:
    r -= A - t
    if r <= 0:
      return 'No'
      
    t = B
    r = min(r + (B - A), N)
    
  return 'Yes'

AB.append([T, T])
print(judge())