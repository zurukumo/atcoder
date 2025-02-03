S = input()

ret = 0
for s in S.split('+') :
    if not '0' in s :
        ret += 1
        
print(ret)