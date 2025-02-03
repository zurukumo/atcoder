K = int(input())
N = 50

a = N + (K // N) + (N - K % N)
ret = [a] * (K % N) + [a-(N+1)] * (N - K % N)
print(N)
print(*ret)