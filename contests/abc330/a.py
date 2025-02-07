N, L = map(int, input().split())
A = [int(i) for i in input().split()]

print(sum(1 if a >= L else 0 for a in A))
