A = input()

i, j = 0, len(A) - 1
count = 0
while i < j :
    if A[i] != A[j] :
        count += 1
    i += 1
    j -= 1
    
if len(A) % 2 == 0 :
    if count == 1 :
        print(25 * len(A) - 2)
    else :
        print(25 * len(A))
else :
    if count == 0 :
        print(25 * (len(A) - 1))
    elif count == 1 :
        print(25 * len(A) - 2)
    else :
        print(25 * len(A))