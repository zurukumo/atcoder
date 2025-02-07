from itertools import product

N = int(input())

for prod in product("abc", repeat=N):
    print("".join(prod))
