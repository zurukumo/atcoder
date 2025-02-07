N, a = map(int, input().split())
k = int(input())
b = [int(i) - 1 for i in input().split()]


def solve():
    # aから見た各単語に行くまでのステップ数
    step = [-1] * N
    step[a - 1] = 0

    # ステップ数に対応する単語
    word = [a - 1]

    cur = a - 1
    while True:
        if step[cur] == k:
            return cur

        if step[b[cur]] == -1:
            step[b[cur]] = step[cur] + 1
            cur = b[cur]
            word.append(cur)

        else:
            a2l = step[b[cur]]
            l2l = step[cur] + 1 - a2l
            return word[a2l + (k - a2l) % l2l]


print(solve() + 1)
