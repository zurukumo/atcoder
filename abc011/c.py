N = int(input())
NG = [int(input()) for _ in range(3)]

def judge() :
	N_ = N

	if N_ in NG :
		return 'NO'

	count = 0
	
	while N_ > 0 :
		if count == 100 :
			return 'NO'

		if not N_-3 in NG :
			N_ -= 3
		elif not N_-2 in NG :
			N_ -= 2
		elif not N_-1 in NG :
			N_ -= 1
		else :
			return 'NO'

		count += 1

	return 'YES'


print(judge())