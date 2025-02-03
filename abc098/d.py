N = int(input())
A = [int(i) for i in input().split()] + [(1 << 21) - 1]

ret = 0
j = 1
cur = A[0]
for i in range(N) :
    while j < N and cur & A[j] == 0 :
        cur ^= A[j]
        j += 1
    ret += j - i
    if j - i == 1 :
        cur = A[j]
        j += 1
    else :
        cur ^= A[i]
    
print(ret)