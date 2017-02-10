# -*- coding: utf-8 -*-

def transpose(X):
	return map(list, zip(*X))

def neighbor(X, m, n):
	m = m / 3 * 3
	n = n / 3 * 3
	return [X[i][j] for j in range(n, n + 3) \
		for i in range(m, m + 3) \
		if X[i][j] != 0]

def candidate(X):
	Y = transpose(X)
	return [[[t for t in range(1, 10) \
		if X[i][j] == 0 and t not in X[i] \
		and t not in Y[j] and t not in neighbor(X, i, j)] \
		for j in range(9)] for i in range(9)]



X = [[5,0,0,0,4,0,9,0,0],
	[0,6,0,0,0,0,0,0,4],
	[0,0,0,0,0,0,1,8,7],
	[1,0,0,0,0,0,0,0,0],
	[0,3,0,1,0,9,0,0,0],
	[4,0,0,7,3,0,0,6,0],
	[0,0,0,6,0,0,3,0,0],
	[0,0,7,0,0,2,0,0,0],
	[0,0,0,8,7,0,5,0,2]]

# print(transpose(X))
# print(neighbor(X, 7, 3))
print(candidate(X))
