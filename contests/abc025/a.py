S = input()
N = int(input()) - 1

print("{}{}".format(S[N // len(S)], S[N % len(S)]))
