N = int(input())
ST = [input().split() for _ in range(N)]


def judge():
    for i in range(N):
        for j in range(i + 1, N):
            if ST[i] == ST[j]:
                return "Yes"

    return "No"


print(judge())
