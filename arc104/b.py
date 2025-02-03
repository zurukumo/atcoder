from collections import defaultdict

N, S = input().split()
N = int(N)

mem = [(0, 0)]

AT, GC = 0, 0
for s in S :
  if s == 'A' : AT += 1
  if s == 'T' : AT -= 1
  if s == 'G' : GC += 1
  if s == 'C' : GC -= 1
  mem.append((AT, GC))
  
ret = 0
for i in range(N + 1) :
  for j in range(i + 1, N + 1) :
    if mem[i][0] == mem[j][0] and mem[i][1] == mem[j][1] :
      ret += 1

print(ret)
  