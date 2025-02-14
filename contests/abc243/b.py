N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

print(sum(1 for a, b in zip(A, B) if a == b))
print(len(set(A) & set(B)) - sum(1 for a, b in zip(A, B) if a == b))
