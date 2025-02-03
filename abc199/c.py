N = int(input())
S = list(input())
Q = int(input())
TAB = [[int(i) for i in input().split()] for _ in range(Q)]

flip = 0
for T, A, B in TAB:
    A -= 1
    B -= 1
    if flip == 1:
        A = (A + N) % (2 * N)
        B = (B + N) % (2 * N)

    if T == 1:
        S[A], S[B] = S[B], S[A]
    else:
        flip = 1 - flip

if flip == 0:
    print("".join(S))
else:
    print("".join(S[N:]) + "".join(S[:N]))
