N = int(input())
S, T = input().split()

U = ''
for s, t in zip(S, T) :
  U += s
  U += t
  
print(U)