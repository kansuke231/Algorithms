from __future__ import division
from random import getrandbits,choice
import math


def mod_exp(x,y,N):

	acc = 1

	while y != 0:
		if y & 1: # if y is odd
			acc = acc*(x%N)
		x = (x**2)%N
		y = y >> 1

	return acc % N

def FermatTest(N):

	a = getrandbits(int(math.log(N,2))+1)

	while a >= N or a == 0:
		a = getrandbits(int(math.log(N,2))+1)

	if mod_exp(a,N-1,N) == 1:
		return True
	else:
		return False

def primality(N):
	if not(N > 1):
		return False
	for i in range(100):
		Flag = FermatTest(N)
		if not Flag:
			return False
	return True

def nextprime(N):
	i = N
	while not primality(i):
		i+=1
	return i

def getrand100():
	MSB = str(choice(range(1,10)))
	others = ""
	for i in range(99):
		others+=str(choice(range(10)))
	return eval(MSB+others)

if __name__ == "__main__":
	#result = nextprime(2015**50)
	#print result
	#print primality(result)
	#result = 0
	#for i in range(1000): # for 1000 samples
	#	s = getrand100()
	#	d = nextprime(s) - s
	#	result+=d
	#	print(i)
	#print result/1000
	# nextprime(2015**50) =
	# 16358840719795595135432271455535002519186833058376927034121246239130110835
	# 54082019822596292891054600336665374484753874781612597488678062518374645151
	# 197910308837890973
	#for e in range(1,500):
	#	if primality(e):
	#		print e
	for e in range(1000):
		if primality(e):
			print e
	#print FermatTest(17)

