N = int(input())
A = [int(i) for i in input().split()]

t = (sum(A[::2])-sum(A[1::2])) // 2
for i in range(N) :
    print(t*2)
    t = A[i] - t