
from collections import defaultdict

def explore(G,v,w,visited,prev,post,clock):
	visited[v] = True
	prev[v] = clock[0]
	clock[0] += 1

	print v,w
	print "clock_prev:",clock
	
	for u,weight in G[v]:
		if not visited[u]:
			explore(G,u,w+weight,visited,prev,post,clock)
		elif visited[u] and (prev[v] > prev[u]): # back edge!
			global minimum
			if minimum > w + weight:
				minimum = w + weight
	post[v]
	clock[0]+=1
	print "clock_post:",clock

def initialize():
	return defaultdict(bool),defaultdict(int),defaultdict(int),[1]

def shortest_cycle(G):

	visited,prev,post,clock = initialize()

	global minimum
	minimum = 10000000 # arbitrarily determined
	
	for v in G.keys():
		explore(G,v,0,visited,prev,post,clock)
		visited,prev,post,clock = initialize()
		print("--"*20)
	print minimum


if __name__ == "__main__":
	G = {"a":[("b",2),("c",4)],
	     "b":[("c",1),("d",4)],
	     "c":[("d",1)],
	     "d":[("a",3),("b",2)]}
	shortest_cycle(G)

