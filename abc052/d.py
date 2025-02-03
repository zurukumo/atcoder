N, A, B = map(int, input().split())
X = [int(i) for i in input().split()]

ret = 0
for i in range(N-1) :
    ret += min((X[i+1] - X[i]) * A , B)
    
print(ret)