R, G, B = map(int, input().split())

ret = float('inf')
for gl in range(-300, 301) :
  tmp = 0
  gr = gl + G - 1
  if gl <= 0 <= gr :
    l, r = abs(gl), abs(gr)
    tmp += l * (l + 1) // 2
    tmp += r * (r + 1) // 2
  else :
    l, r = abs(gl), abs(gr)
    if l < r :
      l -= 1
    else :
      r -= 1
    tmp += abs(l * (l + 1) // 2 - r * (r + 1) // 2)

  rr = min(gl - 1, -100 + (R - 1) // 2)
  rl = rr - R + 1
  if rl <= -100 <= rr :
    l, r = abs(rl + 100), abs(rr + 100)
    tmp += l * (l + 1) // 2
    tmp += r * (r + 1) // 2
  else :
    l, r = abs(rl + 100), abs(rr + 100) - 1
    tmp += abs(l * (l + 1) // 2 - r * (r + 1) // 2)

  bl = max(gr + 1, 100 - (B - 1) // 2)
  br = bl + B - 1
  if bl <= 100 <= br :
    l, r = abs(bl - 100), abs(br - 100)
    tmp += l * (l + 1) // 2
    tmp += r * (r + 1) // 2
  else :
    l, r = abs(bl - 100) - 1, abs(br - 100)
    tmp += abs(l * (l + 1) // 2 - r * (r + 1) // 2)
    
  ret = min(ret, tmp)

print(ret)