N = int(input())
A = [int(i) for i in input().split()]

xor = 0
for a in A:
    xor ^= a

if xor != 0:
    print(-1)
else:
    A.sort()
    while len(A) >= 2 and A[-1] == A[-2]:
        A.pop()
        A.pop()

    if len(A) == 0:
        print(0)
    else:
        print(A[-1] - 1)
