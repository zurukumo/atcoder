A, B, K = map(int, input().split())

if A + K > B - K:
    for i in range(A, B + 1):
        print(i)
else:
    for i in range(A, A + K):
        print(i)
    for i in range(B - K + 1, B + 1):
        print(i)
