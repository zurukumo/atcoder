L, R = map(int, input().split())
S = input()

L -= 1
print(S[:L] + S[L:R][::-1] + S[R:])
