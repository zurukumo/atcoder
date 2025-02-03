import sys
input = sys.stdin.readline

N = int(input())
a = [int(i) for i in input().split()]

color = [0] * 8
over = 0
for i in range(N) :
    if a[i] >= 3200 :
        over += 1
    else :
        color[a[i]//400] += 1

m = 8 - color.count(0)
print(max(1, m), m + over)