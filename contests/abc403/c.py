N, M, Q = map(int, input().split())

view = [set() for _ in range(N + 1)]
all_view = set()
for _ in range(Q):
    query = [int(i) for i in input().split()]
    if query[0] == 1:
        x, y = query[1], query[2]
        view[x].add(y)
    elif query[0] == 2:
        x = query[1]
        all_view.add(x)
    elif query[0] == 3:
        x, y = query[1], query[2]
        if y in view[x] or x in all_view:
            print("Yes")
        else:
            print("No")
