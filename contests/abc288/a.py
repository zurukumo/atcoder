N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N)]

for a, b in AB:
    print(a + b)
