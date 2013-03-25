import math

def calculate_Sqrt(x1, x2, y1, y2):
	X = x2 - x1
	Y = y2 - y1

	length = X ** 2
	height = Y ** 2

	result = math.sqrt (length + height)

	return result

result = calculate_Sqrt(1, 4, 5, 9)
print result