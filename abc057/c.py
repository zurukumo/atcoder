N = int(input())

ret = float('inf')
i = 1
while i * i <= N :
    if N % i == 0 :
        ret = min(ret, len(str(N//i)))
    i += 1
print(ret)