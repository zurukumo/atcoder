x = int(input().replace(" ", ""))


def judge():
    # 計算量
    # x -> Maxで100100
    # i =   1, i * i = 1
    # i =   2, i * i = 4
    #        ………
    # i = 316, i * i = 99856
    # i = 317, i * i = 100489

    for i in range(1, 1000):
        if i * i == x:
            return "Yes"
        if i * i > x:
            break

    return "No"


print(judge())
