N = int(input())
S = input()

flag = True
i = S[0]

if N % 2 == 0 :
    flag = False
elif N % 6 == 1 and i != 'b' :
    flag = False
elif N % 6 == 3 and i != 'a' :
    flag = False
elif N % 6 == 5 and i != 'c' :
    flag = False
else :
    for s in S[1:] :
        if i == 'a' :
            if s != 'b' :
                flag = False
                break
        elif i == 'b' :
            if s != 'c' :
                flag = False
                break
        elif i == 'c' :
            if s != 'a' :
                flag = False
                break
        i = s

if flag :
    print((N - 1) // 2)
else :
    print(-1)
    