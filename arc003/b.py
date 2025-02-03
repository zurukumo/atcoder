N = int(input())
s = [input() for _ in range(N)]

s.sort(key=lambda x: x[::-1])
print('\n'.join(s))