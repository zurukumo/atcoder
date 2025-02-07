P = int(input())

coins = []
x = 1
for i in range(1, 10 + 1):
    x *= i
    for _ in range(100):
        coins.append(x)

s = 0
c = 0
while coins:
    coin = coins.pop()
    if s + coin <= P:
        s += coin
        c += 1

print(c)
