S = input()
N = len(S) + 1

ret = [0] * N
now = 0
for i in range(1, N) :
  if S[i - 1] == '<' :
    now += 1
    ret[i] = now
  else :
    now = 0

now = 0
for i in range(N - 2, -1, -1) :
  if S[i] == '>' :
    now += 1
    ret[i] = max(ret[i], now)
  else :
    now = 0
    
print(sum(ret))