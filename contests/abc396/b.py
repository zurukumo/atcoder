Q = int(input())

card = [0] * 100

for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        x = int(query[1])
        card.append(x)
    else:
        print(card.pop())
