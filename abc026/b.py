import math

N = int(input())
R = [int(input()) for _ in range(N)]
R.sort(reverse=True)

ret = 0
pm = 1
for r in R :
    ret += r * r * pm
    pm *= -1
    
print(ret * math.pi)