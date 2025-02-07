N = int(input())
ABCDE = [int(input()) for _ in range(5)]
m = min(ABCDE)
print(4 - (-N // m))
