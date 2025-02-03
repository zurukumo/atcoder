from itertools import permutations

S1 = list(input())
S2 = list(input())
S3 = list(input())

clist = list(set(S1 + S2 + S3))
for i, c in enumerate(S1):
  S1[i] = clist.index(c)
for i, c in enumerate(S2):
  S2[i] = clist.index(c)
for i, c in enumerate(S3):
  S3[i] = clist.index(c)

if len(set(S1 + S2 + S3)) > 10 :
  print('UNSOLVABLE')
else :
  for perm in permutations(range(10)):
    s1 = 0
    for c in S1:
      s1 *= 10
      s1 += perm[c]
    s2 = 0
    for c in S2:
      s2 *= 10
      s2 += perm[c]
    s3 = 0
    for c in S3:
      s3 *= 10
      s3 += perm[c]
    if s1 + s2 == s3 and s1 != 0 and s2 != 0 and s3 != 0 and len(S1) == len(str(s1)) and len(S2) == len(str(s2)) and len(S3) == len(str(s3)):
      print(s1)
      print(s2)
      print(s3)
      exit()
  
  print('UNSOLVABLE')
