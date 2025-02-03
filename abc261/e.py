N, C = map(int, input().split())
TA = [[int(i) for i in input().split()] for _ in range(N)]

operations = [[0, 1] for _ in range(31)]

for t, a in TA:
    for i in range(31):
        # and
        if t == 1:
            if a & (1 << i):
                operations[i][0] = operations[i][0]
                operations[i][1] = operations[i][1]
            else:
                operations[i][0] = 0
                operations[i][1] = 0
        # or
        elif t == 2:
            if a & (1 << i):
                operations[i][0] = 1
                operations[i][1] = 1
            else:
                operations[i][0] = operations[i][0]
                operations[i][1] = operations[i][1]
        # xor
        elif t == 3:
            if a & (1 << i):
                operations[i][0] = 1 - operations[i][0]
                operations[i][1] = 1 - operations[i][1]
            else:
                operations[i][0] = operations[i][0]
                operations[i][1] = operations[i][1]

    new_c = 0
    for i in range(30, -1, -1):
        new_c <<= 1
        bit = 1 if C & (1 << i) else 0
        new_c += operations[i][bit]
    print(new_c)
    C = new_c
