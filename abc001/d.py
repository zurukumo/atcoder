N = int(input())
SE = [[int(i) for i in input().split('-')] for _ in range(N)]

imos = [0] * 2410

for S, E in SE :
  S -= S % 5
  E = (E + 4) - (E + 4) % 5
  if E % 100 == 60 :
    E += 40
  imos[S] += 1
  imos[E + 1] -= 1

for i in range(1, 2402) :
  imos[i] += imos[i-1]

ret = ''
for i in range(2402) :
  if imos[i] > 0 and imos[i-1] == 0 :
    ret += '{:04d}'.format(i) + '-'
  if imos[i] == 0 and imos[i-1] > 0 :
    ret += '{:04d}'.format(i - 1)
    print(ret)
    ret = ''