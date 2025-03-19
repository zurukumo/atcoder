import bisect


def LongestIncreaseSubsequence(seq):
    lis = [seq[0]]
    for x in seq[1:]:
        if x > lis[-1]:
            lis.append(x)
        else:
            lis[bisect.bisect_left(lis, x)] = x

    return lis
