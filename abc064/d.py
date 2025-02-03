import sys
input = sys.stdin.readline

N = int(input())
S = input()
S = S[:-1]
m = 0
diff = 0
for s in S :
    if s == '(' :
        diff += 1
    elif s == ')' :
        diff -= 1
    m = min(m, diff)
print(('('*(-m))+S+(')'*(diff-m)))