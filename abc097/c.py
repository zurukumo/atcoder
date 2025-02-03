s = input()
K = int(input())

ret = []
slen = len(s)
for i in range(1, 5 + 1) :
    for j in range(slen - i + 1) :
        t = s[j:j+i]
        if not t in ret :
            ret.append(t)
        if len(ret) > K :
            ret.sort()
            ret.pop()
            
print(ret[-1])