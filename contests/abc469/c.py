N = int(input())
S = input()

reversed_s = list(reversed(S))

ret = 0
for _ in range(N):
    while reversed_s:
        last = reversed_s.pop()
        ret += 1
        if last == "x":
            break

    print(ret)
