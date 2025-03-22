N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N)]

AB.sort()
print(sum(AB[-1]))
