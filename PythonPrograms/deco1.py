import time
def t(func):
	def t1(*args,**kwargs):
		st=time.time()
		print("starting time is :",st)
		result=func(*args,**kwargs)
		et=time.time()
		print("ending time is :",et)
		d=et-st
		print("time taken ",d)
		return result
	return t1
@t
def fib():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b
n=int(input("enter the number"))
fibo=fib()
for i in range(n):
	print(next(fibo))
	 
