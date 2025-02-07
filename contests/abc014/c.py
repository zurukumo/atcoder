n = int(input())

sales = [0] * (1000002)

for _ in range(n):
    a, b = map(int, input().split())
    sales[a] += 1
    sales[b + 1] -= 1

for i in range(1000000):
    sales[i + 1] += sales[i]

print(max(sales))
