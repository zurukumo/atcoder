A, B, X = map(int, input().split())

ret = 0
for d in range(11, -1, -1) :
    n = (X - B * d) // A
    if (10 ** d) - 1 <= n :
        ret = max(ret, 10 ** d - 1)
    elif 10 ** (d - 1) <= n <= (10 ** d) - 1 :
        ret = max(ret, n)
        
print(min(ret, 10 ** 9))
    