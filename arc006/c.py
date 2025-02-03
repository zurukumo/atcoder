E = [int(i) for i in input().split()]
B = int(input())
L = [int(i) for i in input().split()]

c = 0
for i in range(6) :
    if L[i] in E :
        c += 1

b = B in L

if c == 6 :
    print('1')

elif c == 5 and b :
    print('2')
    
elif c == 5 :
    print('3')
    
elif c == 4 :
    print('4')
    
elif c == 3 :
    print('5')
    
else :
    print('0')