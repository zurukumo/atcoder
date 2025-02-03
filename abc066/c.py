n = int(input())
a = [int(i) for i in input().split()]

print(*(a[::-2]+a[n%2::2]))