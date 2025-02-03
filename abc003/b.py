S, T = input(), input()

for i in range(len(S)) :
	if (S[i] == '@' and T[i] in '@atcoder') or (T[i] == '@' and S[i] in '@atcoder') or S[i] == T[i] :
		continue
		
	print('You will lose')
	exit()

print('You can win')