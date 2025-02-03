N = int(input())

l = set()
for i in range(0, 101) :
    for j in range(0, 101) :
        l.add(4*i + 7*j)
        
if N in l :
    print('Yes')
else :
    print('No')