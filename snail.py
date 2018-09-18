import math
import pprint

pp = pprint.PrettyPrinter(indent=1)
	
def snail(n):
	res = [ ["x" for i in range(0, n)] for i in range(0, n)]
	
	def square(m, s, l, iter): # matrix, length, iter(start row and column)
		if (l == 1):
			m[iter][iter] = s
		
		if (iter == math.floor(n/2)):
			return m
		
		for i in range (0, l): # up
			m[iter][iter+i] = s + i
		
		for i in range(0, l-2): # right
			m[iter+i+1][iter+l-1] = s+l+i
		
		for i in range(0, l):
			m[iter+l-1][iter+l-1-i] = s+2*l-2+i # bottom
		
		for i in range(1, l-1): # left
			m[i+iter][iter] = s + 4*(l-1) - i
		
		next_start = m[iter+1][iter] + 1
		next_l = l-2
		next_iter = iter + 1
		
		return square(m, next_start, next_l, next_iter)
	
	start = 1
	
	return square(res, start, n, 0)
	
if __name__ == '__main__':
	n = int(input())
	pp.pprint(snail(n))