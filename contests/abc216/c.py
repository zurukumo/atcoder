import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())

print(bin(N)[2:].replace("0", "B").replace("1", "BA"))
