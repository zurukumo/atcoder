import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
S = input()

ret = 0
for i in range(N):
    if S[i] == "x" and (i == 0 or S[i - 1] == "x") and (i == N - 1 or S[i + 1] == "x"):
        ret += 1
print(ret)
