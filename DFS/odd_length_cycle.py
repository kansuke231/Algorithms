# graphs are implemented by dictionary
# {"a":["b","c"],"b":["c"],"c":["d"],"d":["a"]}
import random
from collections import defaultdict

def odd_length_cycle(G):
	# G must be a strongly connected => there must be a cycle
	s = random.choice(G.keys())

	if explore(G,s):
		print "Found an odd-length cycle!"
		return True

	for u in G.keys():
		for v in G[u]:
			if prev[v] > prev[u] + 1:
				if (prev[v] - prev[u])%2==0:
					print "Found an odd-length cycle!!"
					return True

	return False

def explore(G,v):
	visited[v] = True
	global clock
	prev[v] = clock
	clock += 1

	for u in G[v]:
		if visited[u] and (prev[v] > prev[u]): # back edge! 
			if (prev[v] - prev[u])%2==0:
				return True # found an odd-length cycle
		else:
			if not explore(G,u):# if 
				continue
			else:
				return True
	post[v] = clock
	clock += 1
	return False

if __name__ == "__main__":

	G = {"a":["b","h"],"b":["f"],"c":["b"],"d":["c","e"],"e":[],\
	     "f":["c","d","e"],"g":["a","b","f"],"h":["g"]}
	G = {"a":["b"],"b":["c"],"c":["d"],"d":["a"]}
	clock = 1
	visited,prev,post = defaultdict(bool),defaultdict(int),defaultdict(int)

	print odd_length_cycle(G)


