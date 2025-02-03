S = input()
T = input()

x = abs(S.count('L')-S.count('R'))
y = abs(S.count('U')-S.count('D'))
q = S.count('?')

if T == '1' :
    print(x+y+q)
else :
    print(max((x+y+q)%2, x+y-q))