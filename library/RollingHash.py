# ローリングハッシュ
class RollingHash() :
    def __init__(self, S, base=26, mod=2**61-1) :
        hash = [0]
        pow = [1]
        for s in S :
            hash.append((hash[-1] * base + ord(s)) % mod)
            pow.append(pow[-1] * base % mod)

        self.hash = hash
        self.pow = pow
        self.mod = mod
        
    def get(self, l, r) :
        return (self.hash[r+1] - self.hash[l] * self.pow[r+1-l]) % self.mod