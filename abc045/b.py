SA = input()
SB = input()
SC = input()

cur, SA = SA[0], SA[1:]

while True :
    if cur == 'a' :
        if len(SA) == 0 :
            print('A')
            break
        cur, SA = SA[0], SA[1:]
    elif cur == 'b' :
        if len(SB) == 0 :
            print('B')
            break
        cur, SB = SB[0], SB[1:]
    elif cur == 'c' :
        if len(SC) == 0 :
            print('C')
            break
        cur, SC = SC[0], SC[1:]