import re
equation='6x^3 -32x -45'
i=0
equation=re.sub('-','+-',equation)
equation=re.sub('\^','',equation)
print(equation)
a=re.split('[+]',equation)
for p in a:
	b=p.split('x')
	c=[]
	for val in b:
		if(val==' '):
			val='1'
		newval=float(val)
		if newval:
			c.append(newval)
		
	print(c)