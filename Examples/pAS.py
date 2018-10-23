def pAS(A, i, B):
	if i<0:
		print(B)
		return

	C = [A[i]] + B
	pAS(A, i-1, C)
	C = B
	pAS(A, i-1, C)

B = [1]
del B[0]     # B is a empty list now
A = [1, 2, 3]
i = len(A)-1
pAS(A, i, B)
