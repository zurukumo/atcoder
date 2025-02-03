N = int(input())
s = [input() for _ in range(N)]

for i in range(N) :
    print(''.join([s[N-j-1][i] for j in range(N)]))