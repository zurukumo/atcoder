import sys
input = sys.stdin.readline

N = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

class RollingHash() :
    # mod ex. (1<<61)-1, (1<<31)-1
    # 文字列のときはxをordに通すのを忘れない！！
    def __init__(self, x, base=26, mod=(1<<61)-1) :
        self.hash = [0]
        self.pow = [1]
        self.mod = mod
        
        for xi in x :
            self.hash.append((self.hash[-1] * base + xi) % mod)
            self.pow.append(self.pow[-1] * base % mod)
            
    # [l, r)
    def get(self, l, r) :
        return (self.hash[r] - self.hash[l] * self.pow[r-l]) % self.mod

da = [a[i] ^ a[(i + 1) % N] for i in range(N)] * 2
db = [b[i] ^ b[(i + 1) % N] for i in range(N)] * 2

RHa1 = RollingHash(da, base=1<<30)
RHa2 = RollingHash(da, base=1<<30, mod=(1<<31)-1)
RHb1 = RollingHash(db, base=1<<30)
RHb2 = RollingHash(db, base=1<<30, mod=(1<<31)-1)

hashb1 = RHb1.get(0, N)
hashb2 = RHb2.get(0, N)

for i in range(N) :
  if RHa1.get(i, N + i) == hashb1 and RHa2.get(i, N + i) == hashb2 :
    print(i, a[i] ^ b[0])