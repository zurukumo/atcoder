N, K = map(int, input().split())
A = [int(i) for i in input().split()]
A.sort()

s = sum(A)
i = 1
q1 = []
q2 = []
while i * i <= s :
    if s % i == 0 :
        q1.append(i)
        if i * i != s :
            q2.append(s//i)
    i += 1
prime = q2 + q1[::-1]

def solve() :
    for p in prime :
        m = [a%p for a in A]
        m.sort()
        
        dpl = [0] * N
        dpr = [0] * N
        
        dpl[N-1] = p - m[N-1]
        dpr[0] = m[0]
        for i in range(N-2, -1, -1) :
            dpl[i] = dpl[i+1] + p - m[i]
        for i in range(1, N) :
            dpr[i] = dpr[i-1] + m[i]
        n = float('inf')
        for i in range(1, N) :
            n = min(n, max(dpl[i], dpr[i-1]))
        if n <= K :
            return p
            
print(solve())