N = int(input())

ret = 0
for i in range(1, N + 1) :
    if len(str(i)) % 2 == 1 :
        ret += 1
        
print(ret)