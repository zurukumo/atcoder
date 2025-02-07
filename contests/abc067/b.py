N, K = map(int, input().split())
l = [int(i) for i in input().split()]

l.sort()
print(sum(l[-K:]))
