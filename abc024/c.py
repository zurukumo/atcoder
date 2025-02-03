N, D, K = map(int, input().split())
LR = [[int(i) for i in input().split()] for _ in range(D)]
ST = [[int(i) for i in input().split()] for _ in range(K)]

for s, t in ST :
    if s < t :
        for i, (l, r) in enumerate(LR) :
            if l <= s <= r :
                s = r
            if t <= s :
                print(i+1)
                break
    else :
        for i, (l, r) in enumerate(LR) :
            if l <= s <= r :
                s = l
            if s <= t :
                print(i+1)
                break
    