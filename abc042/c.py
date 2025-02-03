N, K = map(int, input().split())
D = [int(i) for i in input().split()]

dec = []
for i in range(10) :
    if not i in D :
        dec.append(str(i))

i = N
while True :
    for j in str(i) :
        if not j in dec :
            break
    else :
        print(i)
        break
        
    i += 1