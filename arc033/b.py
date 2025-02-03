NA, NB = map(int, input().split())
A = set(int(i) for i in input().split())
B = set(int(i) for i in input().split())

print(len(A & B) / len(A | B))