N = int(input())

print(str(N % 9 if N % 9 else 9) * ((N - 1) // 9 + 1))