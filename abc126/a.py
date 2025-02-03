N, K = map(int, input().split())
S = list(input())

S[K-1] = chr(ord(S[K-1]) + 32)

print(''.join(S))
