N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

ret = N
for a in A :
    ret += (D - 1) // a
    
print(ret + X)