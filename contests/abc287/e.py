N = int(input())
S = [input() for _ in range(N)]


trie = {}


def insert(word):
    x1 = 0
    x2 = 0
    for c in word:
        x1 = (x1 * 27 + ord(c) - ord("a") + 1) % (1 << 61)
        x2 = (x2 * 27 + ord(c) - ord("a") + 1) % (1 << 31)
        if (x1, x2) not in trie:
            trie[(x1, x2)] = 1
        else:
            trie[(x1, x2)] += 1


def delete(word):
    x1 = 0
    x2 = 0
    for c in word:
        x1 = (x1 * 27 + ord(c) - ord("a") + 1) % (1 << 61)
        x2 = (x2 * 27 + ord(c) - ord("a") + 1) % (1 << 31)
        if (x1, x2) in trie and trie[(x1, x2)] > 0:
            trie[(x1, x2)] -= 1


def query(word):
    x1 = 0
    x2 = 0
    M = 0
    for i, c in enumerate(word):
        x1 = (x1 * 27 + ord(c) - ord("a") + 1) % (1 << 61)
        x2 = (x2 * 27 + ord(c) - ord("a") + 1) % (1 << 31)
        if (x1, x2) in trie and trie[(x1, x2)] > 0:
            M = max(M, i + 1)
    return M


for s in S:
    insert(s)

for s in S:
    delete(s)
    print(query(s))
    insert(s)
