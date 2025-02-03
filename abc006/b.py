n = int(input())

if n < 3 :
	print(0)
else :
	a, b, c = 0, 0, 1
	
	for _ in range(3, n) :
		a, b, c = b, c, (a + b + c) % 10007
		
	print(c)