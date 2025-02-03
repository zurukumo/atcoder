X, N = map(int, input().split())
p = [int(i) for i in input().split()]

p = set(p)

for i in range(0, 200) :
  if not X - i in p :
    print(X - i)
    break
    
  if not X + i in p :
    print(X + i)
    break