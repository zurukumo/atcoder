N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

if sorted(A) != sorted(B):
    print("No")
elif len(set(A)) != len(A):
    print("Yes")
else:
    idxs = dict()
    for i, a in enumerate(A):
        idxs[a] = i
    B = [idxs[b] for b in B]
    s = 0
    for i in range(N):
        for j in range(i + 1, N):
            if B[j] < B[i]:
                s += 1
    if s % 2 == 0:
        print("Yes")
    else:
        print("No")
