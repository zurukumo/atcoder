D = [int(i) for i in input().split()]
J = [int(i) for i in input().split()]

print(sum(max(d, j) for d, j in zip(D, J)))
