X, Y, A, B = map(int, input().split())

ret = 0
while X * A <= X + B and X * A < Y:
  X *= A
  ret += 1
  
ret += (Y - 1 - X) // B

print(ret)