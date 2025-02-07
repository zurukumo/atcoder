N, Q = map(int, input().split())
lr = [[int(i) - 1 for i in input().split()] for _ in range(Q)]

board = [0] * (N + 1)
for l, r in lr:
    board[l] += 1
    board[r + 1] -= 1
for i in range(1, N):
    board[i] += board[i - 1]
for i in range(N):
    board[i] = str(board[i] % 2)
print("".join(board[:N]))
