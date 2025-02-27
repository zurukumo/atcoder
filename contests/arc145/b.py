N, A, B = map(int, input().split())

if N < A:
    print(0)
    exit()

if A <= B:
    print(N - (A - 1))
    exit()

ret = 0
N -= A - 1
ret = N // A * B
N = N % A
ret += min(N, B)
print(ret)
