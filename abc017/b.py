S = input()
S = S.replace('ch', '').replace('o', '').replace('k', '').replace('u', '')

if S == '' :
    print('YES')
else :
    print('NO')