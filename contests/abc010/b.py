N = int(input())
A = [int(i) for i in input().split()]

result = 0
n_pluck_list = [3, 0, 1, 0, 1, 2]

for a in A:
    result += n_pluck_list[a % 6]

print(result)
