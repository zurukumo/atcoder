T = int(input())

for _ in range(T):
    S = input()
    K = int(input())

    if K % 2 == 1:
        print("First")
        continue

    id = 0
    ids = []
    lefts = []
    is_wrong = False
    for c in S:
        if c == "(":
            ids.append(id)
            lefts.append(id)
            id += 1
        else:
            if lefts:
                ids.append(lefts.pop())
            else:
                is_wrong = True
                break

    if lefts:
        is_wrong = True

    if is_wrong:
        print("First")
        continue

    N = len(S)
    fr = 0
    to = N - 1
    while fr < to and ids[fr] == ids[to]:
        fr += 1
        to -= 1
        N -= 2

    consecutive_l = 0
    consecutive_r = 0

    for i in range(fr, to + 1, 2):
        if ids[i] == ids[i + 1]:
            consecutive_l += 2
        else:
            break

    for i in range(to, fr - 1, -2):
        if ids[i] == ids[i - 1]:
            consecutive_r += 2
        else:
            break

    N -= min(consecutive_l, consecutive_r)

    if N > K:
        print("First")
    else:
        print("Second")
