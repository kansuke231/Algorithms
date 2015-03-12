def search_eql(A,x):
	n = len(A)
	if n == 1:
		if A[0] == x:
			print (x)
			return True
		else:
			return False

	i = n/2
	if A[i] == i + x:
		print(A[i])
		return True
	elif A[i] > i + x:
		return search_eql(A[:i],x)
	else:
		return search_eql(A[i:],i)

if __name__ == "__main__":
	A = [-3,-2,0,2,3,4,5,7,24,50]
	B = [-5,-3,0,1,2,3,4,5,6,7,8,9,12,14,56,78]
	print(search_eql(A,0))

