Deg, Dis = map(int, input().split())

def Dir(d) :
	if 112.5 <= d < 337.5 :
		return 'NNE'
	elif 337.5 <= d < 562.5 :
		return 'NE'
	elif 562.5 <= d < 787.5 :
		return 'ENE'
	elif 787.5 <= d < 1012.5 :
		return 'E'
	elif 1012.5 <= d < 1237.5 :
		return 'ESE'
	elif 1237.5 <= d < 1462.5 :
		return 'SE'
	elif 1462.5 <= d < 1687.5 :
		return 'SSE'
	elif 1687.5 <= d < 1912.5 :
		return 'S'
	elif 1912.5 <= d < 2137.5 :
		return 'SSW'
	elif 2137.5 <= d < 2362.5 :
		return 'SW'
	elif 2362.5 <= d < 2587.5 :
		return 'WSW'
	elif 2587.5 <= d < 2812.5 :
		return 'W'
	elif 2812.5 <= d < 3037.5 :
		return 'WNW'
	elif 3037.5 <= d < 3262.5 :
		return 'NW'
	elif 3262.5 <= d < 3487.5 :
		return 'NNW'
	else :
		return 'N'
	
	
def W(w) :
	w = w / 6
	if 0.5 <= w % 1 :
		w += 1
	w = int(w) / 10
	if 0 <= w <= 0.2 :
		return 0
	elif 0.3 <= w <= 1.5 :
		return 1
	elif 1.6 <= w <= 3.3 :
		return 2
	elif 3.4 <= w <= 5.4 :
		return 3
	elif 5.5 <= w <= 7.9 :
		return 4
	elif 8.0 <= w <= 10.7 :
		return 5
	elif 10.8 <= w <= 13.8 :
		return 6
	elif 13.9 <= w <= 17.1 :
		return 7
	elif 17.2 <= w <= 20.7 :
		return 8
	elif 20.8 <= w <= 24.4 :
		return 9
	elif 24.5 <= w <= 28.4 :
		return 10
	elif 28.5 <= w <= 32.6 :
		return 11
	elif 32.7 <= w :
		return 12

if W(Dis) == 0 :
	print("C 0")
else :
	print("{} {}".format(Dir(Deg), W(Dis)))