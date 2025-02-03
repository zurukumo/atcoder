N = int(input())
S = input()

x = 0
ret = 0

for s in S :
    if s == 'I' :
        x += 1
    else :
        x -= 1
        
    ret = max(ret, x)
    
print(ret)