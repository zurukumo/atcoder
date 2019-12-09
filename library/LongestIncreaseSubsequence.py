from bisect import bisect_left

def LongestIncreaseSubsequence(l) :
    lis = [l[0]]
    for x in l[1:] :
        if x > lis[-1] :
            lis.append(x)
        else :
            lis[bisect_left(lis, x)] = x
    
    return lis