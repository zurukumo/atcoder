T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    S = list(S)
    S.reverse()

    while S and S[-1] == "A":
        S.pop()

    if "A" in S or len(S) == 0:
        print("A")
    else:
        print("B")
