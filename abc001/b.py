N = int(input())

if N < 100 :
	print('00')
elif 100 <= N <= 5000 :
	print('{:02}'.format(int(N / 100)))
elif 6000 <= N <= 30000 :
	print(int(N / 1000 + 50))
elif 35000 <= N <= 70000 :
	print(int((N / 1000 - 30) / 5 + 80))
elif 70000 < N :
	print('89')