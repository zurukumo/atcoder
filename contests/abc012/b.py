N = int(input())

h, N = N // 3600, N % 3600
m, s = N // 60, N % 60

print("{:02d}:{:02d}:{:02d}".format(h, m, s))
