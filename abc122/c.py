N, Q = map(int, input().split())
S = input()
lr = [[int(i) for i in input().split()] for _ in range(Q)]

ac = [0] * N
for i in range(N-1) :
    if S[i:i+2] == 'AC' :
        ac[i] += 1
    ac[i+1] += ac[i]
ac = [0] + ac
    
for l, r in lr :
    print(ac[r-1]-ac[l-1])