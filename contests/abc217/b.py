S = [input() for _ in range(3)]

contests = ["ABC", "ARC", "AGC", "AHC"]
for s in S:
    contests.pop(contests.index(s))

print(contests[0])
