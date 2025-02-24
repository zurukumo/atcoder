N = int(input())
A = [int(i) for i in input().split()]

odd = False
even = False
for i in range(N):
    if A[i] == 1 and i % 2 == 0:
        odd = True
    if A[i] == 1 and i % 2 == 1:
        even = True

if N % 2 == 1:
    odd |= even
    even |= odd

if (odd and even) or N % 4 == 0:
    print("Yes")
else:
    print("No")
