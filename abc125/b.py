N = int(input())
V = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

ret = 0
for i in range(N) :
    ret += max(V[i] - C[i], 0)
    
print(ret)