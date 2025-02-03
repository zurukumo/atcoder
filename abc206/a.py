N = int(input())

N *= 108
N -= N % 100

if N < 20600:
  print('Yay!')
elif N > 20600:
  print(':(')
else:
  print('so-so')