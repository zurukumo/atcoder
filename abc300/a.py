N, A, B = map(int, input().split())
C = [int(i) for i in input().split()]

print(C.index(A + B) + 1)
