N, P, Q = map(int, input().split())
D = [int(i) for i in input().split()]

print(min(P, Q + min(D)))
