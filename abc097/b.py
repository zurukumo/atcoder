X = int(input())

ret = 1
for i in range(2, X + 1) :
    j = i
    while j * i <= X :
        j *= i
        ret = max(ret, j)
print(ret)