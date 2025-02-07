N = int(input())

print("".join("x" if i % 3 == 2 else "o" for i in range(N)))
