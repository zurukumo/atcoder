N = int(input())
T, A = map(int, input().split())
H = [int(i) for i in input().split()]

temp = [abs(A - (T - H[i] * 0.006)) for i in range(N)]
m = min(temp)
print(temp.index(m) + 1)
