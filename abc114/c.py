S = int(input())

def solve() :
    ret = 0
    lst = [0]
    pre, cur = 0, len(lst)
    for _ in range(10) :
        for i in range(pre, cur) :
            for j in [3, 5, 7] :
                s = lst[i]*10+j
                if s > S :
                    return ret
                lst.append(s)
                s = str(s)
                if '3' in s and '5' in s and '7' in s :
                    ret += 1
        pre, cur = cur, len(lst)

print(solve())