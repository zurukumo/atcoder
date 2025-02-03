N = int(input())
a = [int(i) for i in input().split()]

x, y = 0, sum(a)
m = float('inf')

for i in range(N-1) :
    x += a[i]
    y -= a[i]
    m = min(m, abs(x-y))
    
print(m)