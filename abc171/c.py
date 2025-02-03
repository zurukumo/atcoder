N = int(input()) - 1

x = 26
c = 0
while N >= x :
  N -= x
  x *= 26
  c += 1

ret = []
while c >= 0 :
  y = N % 26
  N //= 26
  c -= 1
  ret.append(chr(ord('a') + y)) 

ret = ret[::-1]
print(''.join(ret))