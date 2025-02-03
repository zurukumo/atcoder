M, K = map(int, input().split())

def xor_match(M, K) :
	if K >= 2 ** M :
		return '-1' 

	elif (M, K) == (0, 0) :
		return '0 0'

	elif (M, K) == (1, 0) :
		return '0 0 1 1'

	elif (M, K) == (1, 1) :
		return '-1'

	init = 1

	if K == 0 :
		p_left = [1, 0, 1]
		init = 2
	else :
		p_left = [0, K, 0]

	p_right = []
	for i in range(init, 2**M) :
		if i == K :
			continue
		
		p_right.append(i)

	p = map(str, p_left + p_right + [K] + p_right[::-1])
	return ' '.join(p)

print(xor_match(M, K))