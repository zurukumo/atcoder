S = input()
Q = int(input())
K = [int(i) for i in input().split()]


for ki in K:
    block = (ki - 1) // len(S)
    reverse = False
    x = 2**70
    while block != 0:
        if block >= x:
            reverse = not reverse
            block -= x
        x //= 2

    mod = (ki - 1) % len(S)
    c = S[mod]

    if reverse:
        if c.islower():
            print(c.upper())
        else:
            print(c.lower())
    else:
        print(c)
