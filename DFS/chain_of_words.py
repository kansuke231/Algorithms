from collections import defaultdict

MAXIMUM = 13

def data_import(filename):
	# input: filename
	# output: a list of words
	result = []
	with open(filename,"r") as f:
		for e in f.readlines():
			result.append(e[:-1])
	return result

def isChained(w1,w2):
	# inputs: words considered to be chained
	# 		  w1 shorter than w2 by the length of 1
	# output: Boolean if they can be chained
	if not (len(w1)+1 == len(w2)):
		return False
	return set(list(w1)).issubset(set(list(w2)))

def explore(G,v,depth):
	
	global d
	if G[v] == []:
		if depth > d:
			d = depth
			print("--"*depth + v)
			return True
		else:
			return False

	for u in G[v]:
		if explore(G, u, depth+1):
			print("--"*depth + v)
			return True
		else:
			return False

def DFS(G,groups):
	for i in groups.keys():
		for w in groups[i]:
			if d == MAXIMUM:
				return
			explore(G,w,1)


if __name__ == "__main__":

	words = data_import("wordlst.txt")
	print len(words)
	sorted_words = sorted(words,key=len)

	word_groups = defaultdict(list)
	G = defaultdict(list)

	for w in sorted_words:
		word_groups[len(w)].append(w)

	for k in word_groups.keys()[:-1]:
		for word1 in word_groups[k]:
			for word2 in word_groups[k+1]:
				if isChained(word1, word2):
					G[word1].append(word2)

	global d
	d = 1
	DFS(G,word_groups)

	