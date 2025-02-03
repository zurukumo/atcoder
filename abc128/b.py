N = int(input())

SP = []

for i in range(N):
    S, P = input().split()
    SP.append([i, S, int(P)])

SP.sort(key=lambda x: x[2], reverse=True)
SP.sort(key=lambda x: x[1])

for i in SP:
    print(i[0] + 1)
