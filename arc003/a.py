N = int(input())
r = input()

ret = 0
ret += r.count('A') * 4
ret += r.count('B') * 3
ret += r.count('C') * 2
ret += r.count('D') * 1

print(ret / N)