s = int(input())

def f(n) :
    if n % 2 == 0 :
        return n // 2
    else :
        return 3 * n + 1
        
done = set()
a = s
i = 1
while not a in done :
    done.add(a)
    a = f(a)
    i += 1
print(i)