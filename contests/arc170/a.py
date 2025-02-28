N = int(input())
S = input()
T = input()


ret = 0
space_a = S.count("A") + T.count("A")
space_b = 0
extra_a = 0
for s, t in zip(S[::-1], T[::-1]):
    if s == "A":
        space_a -= 1
    if t == "A":
        space_a -= 1

    if s == "A" and t == "B":
        ret += 1
        if space_a == 0:
            print(-1)
            exit()
        extra_a += 1
    elif s == "B" and t == "A":
        if extra_a > 0:
            extra_a -= 1
        elif space_b > 0:
            ret += 1
        else:
            print(-1)
            exit()

    if s == "B":
        space_b += 1
    if t == "B":
        space_b += 1


print(ret)
