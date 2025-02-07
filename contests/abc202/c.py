from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) - 1 for i in input().split()]

ca = Counter(A)
ret = 0
for c in C:
    ret += ca[B[c]]

print(ret)
