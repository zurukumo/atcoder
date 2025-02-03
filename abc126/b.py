S = input()

A, B = int(S[:2]), int(S[2:])

is_MM_A = 1 <= A <= 12
is_MM_B = 1 <= B <= 12

if is_MM_A and is_MM_B :
	print('AMBIGUOUS')
elif is_MM_A :
	print('MMYY')
elif is_MM_B :
	print('YYMM')
else :
	print('NA')