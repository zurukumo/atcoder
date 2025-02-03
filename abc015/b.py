N = int(input())
A = [int(i) for i in input().split()]

print(-(-sum(A) // (N - A.count(0))))