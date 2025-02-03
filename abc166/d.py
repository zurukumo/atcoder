X = int(input())

def solve() :
  for a in range(-1000, 1000) :
    for b in range(-1000, 1000) :
      if (a ** 5) - (b ** 5) == X :
        return (a, b)
        
print(*solve())