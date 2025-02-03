N = int(input())
A = [int(i) for i in input().split()]

l = len(set(A))
print(l - (N - l) % 2)