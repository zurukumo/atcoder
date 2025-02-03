A, B = map(int, input().split())
S = input()


def solve():
    for i in range(A + B + 1):
        if 0 <= i < A or A + 1 <= i <= A + B:
            if not 48 <= ord(S[i]) <= 57:
                return "No"
        else:
            if S[i] != "-":
                return "No"
    return "Yes"


print(solve())
