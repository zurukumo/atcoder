N = int(input())
a = [int(i) for i in input().split()]

a.sort(reverse=True)
print(sum(a[::2]) - sum(a[1::2]))
