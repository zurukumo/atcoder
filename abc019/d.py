import sys

N = int(input())

cur = 1
Mi, Mv = 0, 0
for i in range(1, N + 1) :
  print('? {0} {1}'.format(cur, i))
  sys.stdout.flush()
  dist = int(input())
  if dist > Mv :
    Mi, Mv = i, dist

cur = Mi
Mi, Mv = 0, 0
for i in range(1, N + 1) :
  print('? {0} {1}'.format(cur, i))
  sys.stdout.flush()
  dist = int(input())
  if dist > Mv :
    Mi, Mv = i, dist

print('! {0}'.format(Mv))