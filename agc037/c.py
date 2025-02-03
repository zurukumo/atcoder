from heapq import heappush, heappop

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

def solve() :
    h = []
    for i in range(N) :
        if A[i] == B[i] :
            continue
        heappush(h, (-B[i], i))

    ret = 0
    while h :
        _, i = heappop(h)
       
        m, M = B[(i-1)%N], B[(i+1)%N]
        if m > M :
            m, M = M, m
        
        if M >= A[i] :
            x = (B[i] + m - 1) // (m + M)
            B[i] -= x * (m + M)
            ret += x
        else :
            if (B[i] - A[i]) % (m + M) != 0 :
                return -1
            ret += (B[i] - A[i]) // (m + M)
            B[i] = A[i]
        
        if A[i] > B[i] :
            return -1
            
        elif A[i] < B[i] :
            heappush(h, (-B[i], i))
    
    return ret
    
print(solve())