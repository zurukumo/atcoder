N = int(input())
A = [int(i) for i in input().split()]

ret = [0] * N
for i, a in enumerate(A) :
    ret[a-1] = i + 1
    
print(*ret)