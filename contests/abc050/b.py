N = int(input())
T = [int(i) for i in input().split()]
M = int(input())

for _ in range(M):
    P, X = map(int, input().split())
    print(sum(T) - T[P - 1] + X)
