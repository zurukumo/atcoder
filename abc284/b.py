T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(i) for i in input().split()]
    print(len([a for a in A if a % 2 == 1]))
