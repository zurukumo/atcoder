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