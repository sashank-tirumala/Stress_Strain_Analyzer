from singularityClass import *
import re 
import matplotlib.pyplot as plt
from sympy import symbols,Integral,N
from sympy.abc import x
class Beam:
	def __init__(self,length,supportType,areaType,YoungsModulus,x=0,y=0,circleradius=0,rectlength=0,rectbreadth=0,Ia=0,Ib=0,IH=0,Ih=0):
		self.loadequation=[]
		self.length=length
		self.supportType=supportType
		self.support1=x
		self.support2=y
		self.shearForceEq=[]
		self.bendingMomentEq=[]
		self.areaType=areaType
		self.deflection=[]
		self.E=YoungsModulus
		self.circleradius=circleradius
		self.rectlength=rectlength
		self.rectbreadth=rectbreadth
		self.Ia=Ia
		self.Ib=Ib
		self.Ih=Ih
		self.IH=IH
	def calcSupportReac(self):
		netLoad=0
		netBendingMoment=0
		integralOfBendingMoment=[]
		for x in self.shearForceEq:
			temp=x.sub(self.length)
			netLoad=netLoad+temp
		for x in self.bendingMomentEq:
			temp=x.integrate()
			integralOfBendingMoment.append(temp)
		for x in integralOfBendingMoment:
			temp=x.sub(self.length)
			netBendingMoment=temp+netBendingMoment
		if(self.supportType=='pin joint'):
			self.getDiscreteForce(self.support1,(netBendingMoment-netLoad*self.support1)*-1/(self.support2-self.support1))
			self.getDiscreteForce(self.support2,(netLoad*self.support2-netBendingMoment)*-1/(self.support2-self.support1))
		if(self.supportType=='cantilever'):
			self.getDiscreteForce(0,-1*netLoad)
			self.getBendingMoment(0,-1*netBendingMoment)

		netBendingMoment=0
		
	def getDiscreteForce(self, dist, magnitude):
		temp = singularity(dist,-1,magnitude)
		self.loadequation.append(temp)

	
	def getContinuousForce(self, leftdist, rightdistance, equation):
		#print(equation)
		equation=re.sub('\^','',equation)
		#print(equation)
		print(equation)
		b=equation.split('x')
		c=[]
		for val in b:
			if(val==''):
				val=1.0
			newval=float(val)
			if newval:
				c.append(newval)
		if(len(c)<2):
			c.append(0)
		temp=singularity(leftdist,c[1],c[0])
		self.loadequation.append(temp)
		if(rightdistance != self.length):
			i=0
			k=self.getKnValues(rightdistance,temp)
			while(i<=temp.exponent):
				temp1=singularity(rightdistance,i,-k[i])
				self.loadequation.append(temp1)
				i=i+1
				
	def getBendingMoment(self,dist,magnitude):
		temp=singularity(dist,-2,magnitude)
		self.loadequation.append(temp)	
	def printLoadEquation(self):
		st=''
		for x in self.loadequation:
			st=st+' '+str(x)
		st=re.sub('\+-','-',st)
		print('Load Equation : ')
		print(st)
	def printShearForceEquation(self):
		st=''
		for x in self.shearForceEq:
			st=st+' '+str(x)
		st=re.sub('\+-','-',st)
		print('Shear Equation : ')
		print(st)
	def printBendingMomentEquation(self):
		st=''
		for x in self.bendingMomentEq:
			st=st+' '+str(x)
		st=re.sub('\+-','-',st)
		print('Bending Moment Equation: ')
		print(st)
	def calcShearForceEq(self):
		self.shearForceEq=[]
		for A in self.loadequation:
			A.coefficientOfFunction=-1*A.coefficientOfFunction
			temp=A.integrate()
			#print(temp)
			self.shearForceEq.append(temp)

	def calcBendingMomentEq(self):
		self.bendingMomentEq=[]
		for A in self.shearForceEq:
			temp=A.integrate()
			self.bendingMomentEq.append(temp)
	
	def plotLoadEq(self):
		x=[x/100.0 for x in range(0,int(self.length*100),1)]
		plotpoints=[0]*int(self.length*100)
		for someValue in self.loadequation:
			currentpoints=someValue.plotpoints(self.length)
			i=0
			while(i<self.length*100-1):
				#print(i)
				plotpoints[i]=plotpoints[i]+currentpoints[i]
				i=i+1
		plt.ylabel('load')
		plt.xlabel('distance')
		plt.plot(x,plotpoints)
		plt.show()
	def plotShearEq(self):
		x=[x/100.0 for x in range(0,int(self.length*100),1)]
		plotpoints=[0]*int(self.length*100)
		for someValue in self.shearForceEq:
			currentpoints=someValue.plotpoints(self.length)
			i=0
			while(i<self.length*100-1):
				#print(i)
				plotpoints[i]=plotpoints[i]+currentpoints[i]
				i=i+1
		plt.ylabel('Shear')
		plt.xlabel('distance')
		plt.plot(x,plotpoints)
		plt.show()
	def plotBendingMomentEq(self):
		x=[x/100.0 for x in range(0,int(self.length*100),1)]
		plotpoints=[0]*int(self.length*100)
		for someValue in self.bendingMomentEq:
			currentpoints=someValue.plotpoints(self.length)
			i=0
			while(i<self.length*100-1):
				#print(i)
				plotpoints[i]=plotpoints[i]+currentpoints[i]
				i=i+1

		plt.plot(x,plotpoints)
		plt.ylabel('Bending Moment')
		plt.xlabel('distance')
		plt.show()

	def plotBendingMomentEqPoints(self):
		x=[x/100.0 for x in range(0,int(self.length*100),1)]
		plotpoints=[0]*int(self.length*100)
		for someValue in self.bendingMomentEq:
			currentpoints=someValue.plotpoints(self.length)
			i=0
			while(i<self.length*100-1):
				#print(i)
				plotpoints[i]=plotpoints[i]+currentpoints[i]
				i=i+1

		return plotpoints
	def getKnValues(self, rightdistance,sng):
		k=[]
		i=0
		j=1
		sngt=sng
		while(i<=sng.exponent):
			tempk=sngt.coefficientOfFunction*((rightdistance-sngt.constant)**sngt.exponent)/j
			j=j*(i+1)
			sngt=sngt.differentiate()
			k.append(tempk)
			i=i+1
		return k
	def maxBendingStress(self):
		plotpts=self.plotBendingMomentEqPoints()
		maxBendingMoment=max(abs(i) for i in plotpts)
		print('Max bending Stress is : ')
		if(self.areaType=='circle'):
			momentOfInertia= 3.14* (self.circleradius**4)/4
			print(maxBendingMoment*self.circleradius/momentOfInertia)
		if(self.areaType=='rectangle'):
			momentOfInertia=self.rectbreadth*(self.rectlength**3)/12
			print(maxBendingMoment*(self.rectlength/2)/momentOfInertia)
		if(self.areaType=='ibeam'):
			momentOfInertia=self.Ia*(self.Ih**3)/12+self.Ib*((self.IH**3)-(self.Ih**3))/12
			print(maxBendingMoment*(self.IH/2)/momentOfInertia)

	def getMomentOfInertia(self):
		if(self.areaType=='circle'):
			#print('entered circle')
			momentOfInertia= 3.14* (self.circleradius**4)/4
			return momentOfInertia
		if(self.areaType=='rectangle'):
			#print('entered rectangle')
			momentOfInertia=self.rectlength*(self.rectlength**3)/12
			return momentOfInertia
		if(self.areaType=='ibeam'):
			#print('entered Ibeam')
			momentOfInertia=self.Ia*(self.Ih**3)/12+self.rectlength*((self.IH**3)-(self.Ih**3))/12
			return momentOfInertia		

	def calcDeflection(self):
		
		temp1=[]
		for A in self.bendingMomentEq:
			temp=A.integrate()
			temp1.append(temp)
		for A in temp1:
			temp=A.integrate()
			self.deflection.append(temp)
		momentOfInertia=self.getMomentOfInertia()
		for A in self.deflection:
			#print(momentOfInertia)
			A.coefficientOfFunction=A.coefficientOfFunction*(1/(self.E*momentOfInertia))
	
	def printDeflection(self):
		st=''
		for x in self.deflection:
			st=st+' '+str(x)
		st=re.sub('\+-','-',st)
		print('Equation of deflection is: ')
		print(st)
	def plotDeflectionPoints(self):
		x=[x/100.0 for x in range(0,int(self.length*100),1)]
		plotpoints=[0]*int(self.length*100)
		for someValue in self.deflection:
			currentpoints=someValue.plotpoints(self.length)
			i=0
			while(i<self.length*100-1):
				#print(i)
				plotpoints[i]=plotpoints[i]+currentpoints[i]
				i=i+1

		return plotpoints
	def maxDeflection(self):
		print('Max deflection is : ')
		print(max(abs(i)for i in self.plotDeflectionPoints()))
	def plotDeflection(self):
		x=[x/100.0 for x in range(0,int(self.length*100),1)]
		plotpoints=[0]*int(self.length*100)
		for someValue in self.deflection:
			currentpoints=someValue.plotpoints(self.length)
			i=0
			while(i<self.length*100-1):
				#print(i)
				plotpoints[i]=plotpoints[i]+currentpoints[i]
				i=i+1
		plt.plot(x,plotpoints)
		plt.ylabel('deflection')
		plt.xlabel('distance')
		plt.show()
		