N = int(input())
MOD = 10 ** 9 + 7

ret = 1
for i in range(2, N + 1) :
    ret *= i
    ret %= MOD
    
print(ret)