N = input()

ret = max(sum(int(n) for n in N), int(N[0]) - 1 + 9 * (len(N) - 1))
print(ret)
