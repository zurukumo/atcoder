T = int(input())
for _ in range(T):
    N = int(input())
    S = input()

    for i in range(1, N):
        if S[i:] > S[:i]:
            print("Yes")
            break
    else:
        print("No")
