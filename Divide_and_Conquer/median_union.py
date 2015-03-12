
def median(A):
	n = len(A)
	if n % 2 != 0:
		return A[n/2]
	else:
		return A[n/2 - 1]

def med_union(A,B):
	
	n_a,n_b = len(A),len(B)
	a = median(A)
	b = median(B)

	if a > b:
		if n_a == 1:
			return B[-1]
		else:
			a = median(A[:n_a/2])
			if b > a:
				return b
			else:
				return med_union(A[:n_a/2],B)
	else:
		if n_b == 1:
			return A[-1]
		else:
			b = median(B[:n_b/2])
			if a > b:
				return a
			else:
				return med_union(A,B[:n_b/2])

if __name__ == "__main__":
	A = [1,100,200,330,490,500,555]
	B = [2,198,234,454,890,990,1234]
	print med_union(A,B)
	print sorted(A + B)
	print(median(sorted(A+B)))




