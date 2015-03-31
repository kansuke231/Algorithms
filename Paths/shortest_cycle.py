
from collections import defaultdict

def explore(G,v,w,visited,prev,clock):
	visited[v] = True
	prev[v] = clock
	clock += 1

	print v,w
	
	for u,weight in G[v]:
		if not visited[u]:
			explore(G,u,w+weight,visited,prev,clock)
		elif visited[u] and (prev[v] > prev[u]): # back edge!
			global minimum
			if minimum > w + weight:
				minimum = w + weight

def initialize():
	return defaultdict(bool),defaultdict(int),0

def shortest_cycle(G):

	visited,prev,clock = initialize()

	global minimum
	minimum = 10000000 # arbitrarily determined
	
	for v in G.keys():
		explore(G,v,0,visited,prev,clock)
		visited,prev,clock = initialize()
		print("--"*20)
	print minimum


if __name__ == "__main__":
	G = {"a":[("b",2),("c",4)],
	     "b":[("c",1),("d",4)],
	     "c":[("d",1)],
	     "d":[("a",3),("b",2)]}
	shortest_cycle(G)

