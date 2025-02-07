n, m = map(int, input().split())
rad = (n * 30 + m / 2 - m * 6) % 360
print(min(rad, 360 - rad))
