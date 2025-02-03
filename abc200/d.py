N = int(input())
A = [int(i) for i in input().split()]

def solve():
  mem = dict()
  mem[0] = []
  
  for i, a in enumerate(A) :
    mem_ = mem.copy()
    for k, v in mem.items():
      nk = (k + a) % 200
      nv = v + [i + 1]
      if nk in mem_ and mem_[nk] != []:
        print('Yes')
        print(len(nv), *nv)
        print(len(mem_[nk]), *mem_[nk])
        return
      else :
        mem_[nk] = nv
        
    mem = mem_.copy()
        
  print('No')
  return
  
solve()