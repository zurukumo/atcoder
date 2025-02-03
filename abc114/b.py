S = input()

ret = float('inf')
for i in range(len(S) - 2) :
    ret = min(ret, abs(int(S[i:i+3])-753))
print(ret)