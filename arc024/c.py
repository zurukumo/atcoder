N = int(input())
color = [int(input()) for _ in range(N)]

if sum(color) == 0 or sum(color) == N :
    print(-1)

else :
    color = color * 2

    ret = 0
    pre = -1
    count = 0
    for c in color :
        if c == pre :
            count += 1
        else :
            ret = max(ret, count)
            count = 1
            pre = c
            
    print((ret + 1) // 2)