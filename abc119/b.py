N = int(input())

ret = 0
for _ in range(N) :
    x, u = input().split()
    x = float(x)

    if u == 'JPY' :
        ret += x
    else :
        ret += x * 380000
print(ret)