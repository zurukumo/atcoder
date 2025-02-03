N = int(input())
SP = [input().split() for _ in range(N)]
    
half = sum([int(p) for _, p in SP]) / 2

for s, p in SP :
    if int(p) > half :
        print(s)
        break
else :
    print('atcoder')