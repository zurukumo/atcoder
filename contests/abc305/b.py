p, q = input().split()

dist = {"A": 0, "B": 3, "C": 4, "D": 8, "E": 9, "F": 14, "G": 23}
print(abs(dist[p] - dist[q]))
