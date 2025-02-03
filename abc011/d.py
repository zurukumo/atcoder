N, D = map(int, input().split())
X, Y = map(int, input().split())

def solve() :
  if X % D != 0 and Y % D != 0 :
    return 0
    
  x1 = abs(X) // D
  y1 = abs(Y) // D
  rest = N - x1 - y1
  
  if x1 + y1 > N or rest % 2 != 0 :
    return 0
  
  fac = [1]
  for i in range(1, N + 1) :
    fac.append(fac[-1] * i)
    
  def comb(n, r) :
    return fac[n] // (fac[n-r] * fac[r])
  
  ret = 0
  for x2 in range(0, rest + 1, 2) :
    y2 = rest - x2
    x, y = x1 + x2, y1 + y2
    ret += comb(N, x) * comb(x, x2//2) * comb(N-x, y2//2) / (4 ** N)
    
  return ret
  
print(solve())