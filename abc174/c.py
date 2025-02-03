K = int(input())

done = set()
i = 0
x = 7
flag = True
while x % K != 0:
    if not x in done:
        done.add(x)
    else:
        flag = False
        break
    x = (x % K) * 10 + 7
    i += 1

if flag:
    print(i + 1)
else:
    print(-1)
