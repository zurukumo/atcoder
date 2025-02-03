N = int(input())
W = [input() for _ in range(N)]


def check():
    siri = W[0][-1]
    double = [W[0]]
    for i in range(1, N):
        if W[i] in double:
            return "No"
        double.append(W[i])

        atama = W[i][0]
        if atama != siri:
            return "No"

        siri = W[i][-1]
    return "Yes"


print(check())
