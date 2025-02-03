L, H = map(int, input().split())
N = int(input())
A = [int(input()) for _ in range(N)]

for a in A :
    if a < L :
        print(L-a)
    elif L <= a <= H :
        print(0)
    else :
        print(-1)