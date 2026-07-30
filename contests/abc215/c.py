import itertools

S, K = input().split()
K = int(K)

words = set()
for indexes in itertools.permutations(range(len(S))):
    s = ""
    for index in indexes:
        s += S[index]
    words.add(s)

sorted_words = sorted(list(words))
print(sorted_words[K - 1])
