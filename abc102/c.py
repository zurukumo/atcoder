N = int(input())
A = [int(i) for i in input().split()]

for i in range(N) :
    A[i] -= i + 1
A.sort()

mid = A[N // 2]
print(sum([abs(A[i] - mid) for i in range(N)]))