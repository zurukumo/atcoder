K = int(input())
S = [int(i) for i in input()[:4]]
T = [int(i) for i in input()[:4]]

rest = [K] * 10
for i in range(10) :
  rest[i] -= S.count(i) + T.count(i)

ret = 0
for i in range(1, 10) :
  for j in range(1, 10) :
    stmp = S + [i]
    ttmp = T + [j]
    spoint = sum([k * (10 ** stmp.count(k)) for k in range(10)])
    tpoint = sum([k * (10 ** ttmp.count(k)) for k in range(10)])
    
    if spoint > tpoint :
      if i == j and rest[i] >= 2 :
        ret += rest[i] * (rest[j] - 1)
      elif i != j and rest[i] >= 1 and rest[j] >= 1 :
        ret += rest[i] * rest[j]
 
print(ret / ((9 * K - 8) * (9 * K - 9)))
   