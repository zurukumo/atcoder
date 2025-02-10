N = [int(i) for i in input()]

if N == sorted(N, reverse=True) and len(N) == len(set(N)):
    print("Yes")
else:
    print("No")
