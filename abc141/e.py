N = int(input())
S = input()

mod = 10 ** 9 + 7
hash = [0]
pow = [1]
for s in S :
    hash.append((hash[-1] * 26 + ord(s) - 97) % mod)
    pow.append(pow[-1] * 26 % mod)

M = 0
for i in range(N + 1) :
    for j in range(i + 1, N + 1) :
        for k in range(M + 1, N - j + 1) :
            if i + k > j :
                break
            if (hash[j+k] - hash[j] * (pow[k])) % mod == (hash[i+k] - hash[i] *  pow[k]) % mod :
                M += 1
            else :
                break
                
print(M)