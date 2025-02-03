from collections import Counter

N = int(input())
a = [int(i) for i in input().split()]

k, v = list(Counter(a).keys()), list(Counter(a).values())
if len(k) == 3 and k[0] ^ k[1] == k[2] and v[0] == v[1] == v[2] :
    print('Yes')
elif len(k) == 2 and ((k[0] == 0 and v[0] * 2 == v[1]) or (k[1] == 0 and v[1] * 2 == v[0])) :
    print('Yes')
elif len(k) == 1 and k[0] == 0 :
    print('Yes')
else :
    print('No')