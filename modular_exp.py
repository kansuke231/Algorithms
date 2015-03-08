import math

def mod_exp(x,y,N):

	acc = 1

	while y != 0:
		if y & 1: # if y is odd
			acc = acc*(x%N)
		x = (x**2)%N
		y = y >> 1

	return acc % N
