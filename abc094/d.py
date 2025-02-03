n = int(input())
a = [int(i) for i in input().split()]

a.sort()
M1, M2 = 0, 0
for i in range(n) :
    m = min(a[i], a[-1] - a[i])
    if m > M2 :
        M1, M2 = a[i], m
    
print(a[-1], M1)