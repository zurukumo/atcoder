N = int(input())
S = input()
T = input()

if sorted(S) != sorted(T):
    print(-1)
    exit()

S = list(S)
T = list(T)

while S and T:
    if S[-1] == T[-1]:
        S.pop()
        T.pop()
    else:
        T.pop()

print(len(S))
