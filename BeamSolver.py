from sympy import *
from operator import itemgetter
externalDiscreteForces=[]
externalContinousForces=[]
externalSupports=[]
externalMoments=[]
allforces=[]
x= symbols("x")
allobstacles={}
i=0
lengthOfBeam=float(input("Mention length of the beam: "))
print('The conventions are downward positive and clockwise positive, all distances in metres')
print('Start mentioning distances of support from left end')
while(i<2):		
	temp1=int(input())
	temp={}
	temp['leftend']=temp1
	temp['rightend']=temp1
	temp['magnitude']=0
	externalSupports.append(temp)

	i=i+1
temp=int(input('Please specify number of external discrete forces '))
i=0
print('Start mentioning distances of force from left end and then its magnitude in newtons')
while(i<temp):		
	temp1=eval(input())
	temp2=eval(input())
	forceinfo={}
	forceinfo['leftend']=temp1
	forceinfo['rightend']=temp1
	forceinfo['magnitude']=temp2
	externalDiscreteForces.append(forceinfo)
	print('Moving on to next')
	allforces.append(forceinfo)
	i=i+1

temp=int(input('Please specify number of external continous forces: '))
i=0

while(i<temp):	
	temp1=eval(input("Where does continuous force start from left side: "))
	forceinfo={}
	forceinfo['leftend']=temp1
	temp1=eval(input("Where does continuous force end from left side: "))
	forceinfo['rightend']=temp1
	temp1=input("What is equation of continuous force: (in terms of x only) ")
	forceinfo['expression']=sympify(temp1)
	externalContinousForces.append(forceinfo)
	allforces.append(forceinfo)
	print('Moving on to next')
	i=i+1
temp=int(input('Please specify number of external moments: '))
i=0
print('Start mentioning distances of moments from left end and then its magnitude in Nm')
while(i<temp):		
	temp1=eval(input())
	temp2=eval(input())
	forceinfo={}
	forceinfo['leftend']=temp1
	forceinfo['rightend']=temp1
	forceinfo['magnitude']=temp2
	externalMoments.append(forceinfo)
	allforces.append(forceinfo)
	i=i+1
print('ES:',externalSupports)
print('EM:',externalMoments)
print('ECF:',externalContinousForces)
print('EDF:',externalDiscreteForces)

n1, n2 = symbols("Ny1 Ny2")
sum=0
for y in externalDiscreteForces:
	sum=sum+y['magnitude']

for y in externalContinousForces:
	print(y['expression'])
	
	tempsum = integrate(y['expression'],(x,y['leftend'],y['rightend']))
	sum=sum+tempsum


firsteq= n1+n2 + sum

pprint(firsteq)
sum=0
for y in externalDiscreteForces:
	temp= y['leftend']*y['magnitude']
	sum=sum+temp

for y in externalContinousForces:
	newexp=y['expression']*x
	pprint(newexp)
	tempsum=integrate(newexp,(x,y['leftend'],y['rightend']))
	sum=sum+tempsum

for y in externalMoments:
	sum=sum+y[1]

secondeq= n1*externalSupports[0]['leftend']+n2*externalSupports[1]['leftend'] + sum
pprint(secondeq)
soln=solve([firsteq, secondeq],(n1,n2),dict=True)
externalSupports[0]['magnitude']=soln[0][n1]
externalSupports[1]['magnitude']=soln[0][n2]
allforces.append(externalSupports[0])
allforces.append(externalSupports[1])
sortedforces=sorted(allforces,key=itemgetter('leftend','rightend'))
print(sortedforces)
vsfend=0
vsfexp=[]
vsf=symbols('Shear-Force')
x=symbols('x')
i=0
for a in sortedforces:
	if (a['rightend']!=a['leftend']):
		exprdetails={}
		exprdetails['eqleftend']=a['leftend']
		exprdetails['eqrightend']=a['rightend']
		temp=integrate(a['expression'],x)
		print(temp)
		temp1=temp.subs(x,a['leftend'])
		temp=temp-temp1
		print(temp)
		expr= vsf-vsfend+temp
		exprdetails['expression']=sympify(expr)
		vsfexp.append(exprdetails)
		expr=exprdetails['expression'].subs(x,a['rightend'])
		vsfend=solve(expr,vsf)[0]
	else:
		exprdetails={}
		exprdetails['eqleftend']=a['leftend']
		if(i>=len(allforces)-1):
			exprdetails['eqrightend']=lengthOfBeam
		else:
			exprdetails['eqrightend']=sortedforces[i+1]['leftend']
		print(a['magnitude'],vsf,vsfend)
		expr= vsf-vsfend+a['magnitude']
		exprdetails['expression']=expr
		expr=expr.subs(x, a['leftend'])
		vsfexp.append(exprdetails)
		vsfend=solve(expr,vsf)[0]
	i=i+1
pprint(vsfexp)




