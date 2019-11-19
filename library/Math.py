# 最大公約数
def gcd(a, b) :
    if b > a : a, b = b, a
    while b != 0 :
        a, b = b, a % b
    return a
    
# 最小公倍数
def lcm(a, b) :
    return a * b // gcd(a, b)