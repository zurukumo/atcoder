N = int(input())
A = [int(input()) for _ in range(N)]

from bisect import bisect_right
	
def LIS(L) :   
    lis = [L[0]]
    for a in L[1:] :
        if a >= lis[-1] :
            lis.append(a)
        else :
            s = bisect_right(lis, a)
            lis[s] = a
    return len(lis)

print(LIS(A[::-1]))