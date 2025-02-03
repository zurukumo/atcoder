N = int(input())
S = input() + '.'

pre = S[0]
ret = 0
for s in S :
    if s != pre :
        ret += 1
        pre = s
print(ret)