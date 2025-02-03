N, A, B, C, D = map(int, input().split())
S = input()

def check() :
    if '##' in S[A-1:C] or '##' in S[B-1:D] :
        return 'No'

    if C < D or '...' in S[B-2:D+1] :
        return 'Yes'

    return 'No'
        

print(check())