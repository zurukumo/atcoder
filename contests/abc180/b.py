N = int(input())
x = [int(i) for i in input().split()]

print(sum([abs(xi) for xi in x]))
print(sum([xi * xi for xi in x]) ** 0.5)
print(max([abs(xi) for xi in x]))
