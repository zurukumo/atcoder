from collections import Counter

N = int(input())
a = [int(i) for i in input().split()]

def solve() :
    cnt = list(Counter(a).items())
    cnt.sort()
    
    if cnt[0][1] == 1 and cnt[-1][0] != 2 * cnt[0][0] :
        return 'Impossible'
    if cnt[0][1] == 2 and cnt[-1][0] != 2 * cnt[0][0] - 1 :
        return 'Impossible'
    if cnt[0][1] > 2 :
        return 'Impossible'

    for i in range(1, len(cnt)) :
        if cnt[i][0] != cnt[i-1][0] + 1 :
            return 'Impossible'
        if cnt[i][1] < 2 :
            return 'Impossible'
            
    return 'Possible'
    
print(solve())