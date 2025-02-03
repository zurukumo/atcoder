N = int(input())
A = [int(i) for i in input().split()]

ret = [0] * N
for a in A:
    ret[a - 1] += 1

for i in range(N):
    print(ret[i])
