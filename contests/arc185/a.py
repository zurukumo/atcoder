T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    s = N * (N + 1)
    if 0 < s % M <= N:
        print("Bob")
    else:
        print("Alice")
