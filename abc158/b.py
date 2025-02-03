N, A, B = map(int, input().split())

ret = (N // (A + B)) * A
ret += min(A, N % (A + B))

print(ret)