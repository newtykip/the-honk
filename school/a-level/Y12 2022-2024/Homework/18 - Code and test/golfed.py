from random import randint as r
from functools import reduce
from operator import iconcat
a,p=range,print

def q(p,e,v):
	while True:
		try:
			value = int(input(p))
			if v and v(value):raise ValueError
			return value
		except ValueError:p(e)

def g(n,a,b):
	if a > b:raise ValueError('Minimum value must be less than maximum value!');return[[r(a,b)for _ in a(n)]for _ in a(n)]

def o(m):
	n,r,d=len(m),"{:^7}| "*n,'-'*(n*9-1);p(d);[p(f'{r.format(*x)}\n{d}')for x in m]

def s(m,l=True):
	s,n=0,len(m);[(s:=s+x[i])if l else(s:=s+x[n-i-1])for i,x in enumerate(m)];return s 

def d(m):
	l,x=s(m),s(m, False)
	
	return abs(x-l)

def c(m):
	n=len(m)-1;return m[0][0]+m[0][n]+m[n][0]+m[n][n]

a,n=lambda m:sum(reduce(iconcat,m,[]))/(len(m)**2),q('Please enter the dimension of the square matrix: ','Please enter a natural number greater than 1.',lambda x:x<=1);m=g(n,1,100);z,x,k=d(m),c(m),a(m);o(m)
p(f"""Diagonal difference: {z}
Sum of the corners: {x}
Average value: {k}""")
