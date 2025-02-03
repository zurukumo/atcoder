N, va, vb, L = map(int, input().split())

print("{:.8f}".format(L * pow(vb, N) / pow(va, N)))
