N, A, B = map(int, input().split())
S = [int(input()) for _ in range(N)]

if max(S) != min(S) :
    P = B / (max(S) - min(S))
    Q = A - P * sum(S) / N
    print(P, Q)
else :
    print(-1)