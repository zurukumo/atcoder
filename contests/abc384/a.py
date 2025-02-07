N, c1, c2 = input().split()
N = int(N)
S = input()

print("".join((c1 if c == c1 else c2 for c in S)))
