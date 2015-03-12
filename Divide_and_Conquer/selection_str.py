from __future__ import division
import random
from median_union import median
from math import ceil

def subarrays(S,v):
	SL = []
	SR = []
	for word in S:
		if word < v:
			SL.append(word)
		elif word > v:
			SR.append(word)
	return SL,SR

def selection(S,k):

	if len(S) == 1:
		#print S[0]
		return 0
	v = random.choice(S)
	SL,SR = subarrays(S,v)
	
	while not(len(S)/4 <= len(SL) and len(SL) <= 3*len(S)/4):
		v = random.choice(S)
		SL,SR = subarrays(S,v)

	if k <= len(SL):
		return selection(SL,k) + 1
	elif len(SL) < k and k <= len(SL) + 1:
		#print v
		return 0
	else:
		return selection(SR,k-len(SL)-1)

if __name__ == "__main__":
	S = []
	with open("wordlst.txt","r") as f:
		for e in f.readlines():
			S.append(e[:-1])
	results = []
	for e in range(1000):
		results.append(selection(S,ceil(len(S)/2)))
	print(min(results))
	print(max(results))
	print(sum(results)/1000)

	print(median(sorted(S)))
