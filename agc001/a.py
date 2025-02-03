N = int(input())
L = [int(i) for i in input().split()]

L.sort()
print(sum(L[0::2]))