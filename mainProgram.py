from BeamClass import *
length=int(input('Please enter the length of the beam: '))
supportType=input('Please enter the support reaction type, either pin joint or cantilever: ')
supportType=supportType.replace(' ','')
supportType=supportType.replace('-','')
supportType=supportType.lower()
if(supportType=='pinjoint'):
	x=float(input('Please enter distance of first support from left end: '))
	y=float(input('Please enter distance of second support from left end: '))
else:
	x=0
	y=0
youngsmodulus=float(input('Please enter Youngs Modulus of the material of the beam: '))
areaType=input('Please enter the cross-section area of the beam: ')
areaType=areaType.replace(' ','')
areaType=areaType.replace('-','')
areaType=areaType.lower()
if(areaType=='rectangle'):
	breadth=float(input('Please enter breadth of the rectangle: '))
	height=float(input('Please enter height of the rectangle: '))
	newBeam=Beam(length,supportType,areaType,youngsmodulus,x,y,0,breadth,height)
elif(areaType=='circle'):
	radius=float(input('Please enter radius of the circle: '))
	newBeam=Beam(length,supportType,areaType,youngsmodulus,x,y,radius)

elif(areaType=='ibeam'):
	H=float(input('Please enter total height of I beam : '))
	h=float(input('Please enter smaller height of I beam: '))
	b=float(input('Please enter larger breadth of I beam: '))
	a=float(input('Please enter smaller b readth of I beam: '))
	newBeam=Beam(length,supportType,areaType,youngsmodulus,x,y,0,0,0,a,b,H,h)
i=0
no=float(input('Please enter number of discrete forces on the beam: '))
while(i<no):
	dist=float(input('Please enter its distance from left end: '))
	mag=float(input('Please enter magnitude of the force: '))
	newBeam.getDiscreteForce(dist,mag)
	i=i+1
no=float(input('Please enter number of continuous forces: '))
i=0
while(i<no):
	left=float(input('Please enter leftend from which force starts: '))
	right=float(input('Please enter rightend where force terminates: '))
	equation=input('Please enter equation of the force: ')
	equation=equation.replace('-','+-')
	equation=equation.split('+')
	for everyPart in equation:
		newBeam.getContinuousForce(left,right,everyPart)
	i=i+1
i=0
no=float(input('Please enter number of discrete moments on the beam: '))
while(i<no):
	dist=float(input('Please enter its distance from left end: '))
	mag=float(input('Please enter magnitude of the moment: '))
	newBeam.getBendingMoment(dist,mag)
	i=i+1
newBeam.calcShearForceEq()
newBeam.calcBendingMomentEq()
newBeam.calcSupportReac()
newBeam.calcShearForceEq()
newBeam.calcBendingMomentEq()
newBeam.calcDeflection()
newBeam.printLoadEquation()
newBeam.printShearForceEquation()
newBeam.printBendingMomentEquation()
newBeam.plotLoadEq()
newBeam.plotShearEq()
newBeam.plotBendingMomentEq()
if(newBeam.supportType=='cantilever'):
	newBeam.plotDeflection()
	newBeam.maxDeflection()
