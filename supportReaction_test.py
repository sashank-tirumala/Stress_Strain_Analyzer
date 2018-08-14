from BeamClass import *
a=Beam(6,'Pin Joint',0,6)
a.getContinuousForce(0,6,'10x^0')
a.calcShearForceEq()
a.calcBendingMomentEq()
a.calcSupportReac()
a.printLoadEquation()