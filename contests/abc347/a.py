N, K = map(int, input().split())
A = [int(i) for i in input().split()]

print(*(a // K for a in A if a % K == 0))
