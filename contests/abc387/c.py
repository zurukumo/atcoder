L, R = map(int, input().split())


def count(n):
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10
    digits.reverse()

    old_dp = [[0, 0] for _ in range(10)]
    for i in range(1, 10):
        if i < digits[0]:
            old_dp[i][0] = 1
        elif i == digits[0]:
            old_dp[i][1] = 1

    for d in digits[1:]:
        new_dp = [[0, 0] for _ in range(10)]
        for i in range(1, 10):
            new_dp[i][0] = 1

        for i in range(10):
            for j in range(i):
                if j < d:
                    new_dp[i][0] += old_dp[i][0] + old_dp[i][1]
                elif j == d:
                    new_dp[i][0] += old_dp[i][0]
                    new_dp[i][1] += old_dp[i][1]
                elif j > d:
                    new_dp[i][0] += old_dp[i][0]
        old_dp = new_dp

    return sum(sum(row) for row in old_dp)


print(count(R) - count(L - 1))
