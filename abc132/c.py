N = int(input())
d = [int(i) for i in input().split()]

if N % 2 == 1 :
    print(0)
else :
    d.sort()
    print(d[N//2]-d[N//2-1])