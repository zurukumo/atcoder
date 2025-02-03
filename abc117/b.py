N = int(input())
L = [int(i) for i in input().split()]

if 2 * max(L) < sum(L) :
    print('Yes')
else :
    print('No')