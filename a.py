from math import log

P = float(input())
x = 1.5 * (log(log(2) * P / 1.5)) / log(2)
y = x + P / pow(2, x / 1.5)

if x > 0 :
    print(y)
else :
    print(P)