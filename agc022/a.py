S = [ord(i) for i in input()] + [96]

def solve() :
  for i in range(len(S) - 1, -1, -1) :
    for j in range(S[i] + 1, 97 + 26) :
      if not j in S[:i+1] :
        S[i] = j
        return ''.join(map(chr, S[:i+1]))
  return -1

print(solve())