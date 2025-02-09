N = int(input())
A = [int(i) for i in input().split()]

set_a = set(A)
for i in range(1, 1001):
    if i - 1 in set_a and i not in set_a and i + 1 in set_a:
        print(i)
