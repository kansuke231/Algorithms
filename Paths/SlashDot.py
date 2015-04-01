
import numpy as np
from collections import defaultdict
from functools import partial

def data_import(file):
	# input -> filename (string)
	# output -> a list of edges (e.g. [(1,34),(3,67),....])
	output = []
	with open(file,"r") as f:
		for e in f.readlines():
			output.append(tuple(map(int,e.split("\n")[0].split("\t"))))
	return output

def Graph(edge_list):
	# input -> a list of edges
	# output -> two dictionaries G and G_R whose values are numpy.array object
	
	G = defaultdict(partial(np.ndarray, 0))
	G_R = defaultdict(partial(np.ndarray, 0)) # reversed graph
	for u,v in edge_list:
		G[u] = np.append(G[u],v)
		G_R[v] = np.append(G_R[v],u)

	return G,G_R

def initialize():
	# output -> visited,prev,post,clock(a list object)
	return defaultdict(bool),defaultdict(int),defaultdict(int),[1]

def explore(G,v,visited,prev,post,ccnum,cc,clock):
	visited[v] = True
	prev[v] = clock[0]
	ccnum[v] = cc
	clock[0]+=1

	for u in G[v]:
		if not visited[u]:
			explore(G, u, visited, prev, post, ccnum, cc, clock)

	post[v] = clock[0]
	clock[0]+=1

def DFS(G,visited,prev,post,clock,nodes_sorted=[]):
	
	ccnum = defaultdict(int)
	cc = 1

	if not nodes_sorted:
		nodes = G.keys()
	else:
		nodes = nodes_sorted

	for v in nodes:
		if not visited[v]:
			explore(G, v, visited, prev, post, ccnum, cc, clock)
			cc += 1

	return ccnum

def group(ccnum):
	inv_map = {}
	for k, v in ccnum.iteritems():
	    inv_map[v] = inv_map.get(v, [])
	    inv_map[v].append(k)
	return inv_map

def largest_scc(components):
	return max(components.items(),key=lambda x:len(x[1]))[1]

def component_edges(G,component):
	output = []
	for e in component:
		for u in G[e]:
			if u in component:
				output.append((e,u))
	return output


def main():
	# "soc-Slashdot0811.txt"
	edge_list = data_import("example.txt")
	G,G_R = Graph(edge_list)
	visited_R, prev_R, post_R, clock_R = initialize()

	DFS(G_R,visited_R,prev_R,post_R,clock_R)

	post_sorted = [k for k,v in  sorted(post_R.items(),key = lambda x:x[1],reverse=True)]
	visited, prev, post, clock = initialize()

	ccnum = DFS(G, visited, prev, post, clock, post_sorted)

	largest = largest_scc(group(ccnum))
	largest_edges = component_edges(G,largest)
	print("nodes:",largest)
	print("number of nodes: %d"%len(largest))
	print("-"*100)
	print("edges:",largest_edges)
	print("number of edges: %d"%len(largest_edges))

if __name__ == "__main__":
	main()

