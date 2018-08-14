from BeamClass import *
from sympy import *
newBeam=Beam(8,'cantilever',0,8)
newBeam.getDiscreteForce(2,1000)
newBeam.getDiscreteForce(6,800)
newBeam.getContinuousForce(2,6,'200x^0')
newBeam.calcShearForceEq()
newBeam.calcBendingMomentEq()
newBeam.calcSupportReac()
newBeam.calcShearForceEq()
newBeam.calcBendingMomentEq()
newBeam.printLoadEquation()
newBeam.printShearForceEquation()
newBeam.printBendingMomentEquation()
newBeam.plotLoadEq()
newBeam.plotShearEq()
newBeam.plotBendingMomentEq()
# # def calSupportReaction(concForce,concMoment,distributedForce,distSupport,support_type):
#     sumforce = 0
#     summoment = 0
#     x = Symbol('x')
#     for i in range(0,len(concForce)):
#         sumforce += concForce[i][0]
#         summoment += concForce[i][0]*concForce[i][1]
#     for i in range(0,len(concMoment)):
#         summoment += concMoment[i][0]
#     for i in range(0,len(distributedForce)):
#         sumforce += N(integrate(distributedForce[i][0],(x,distributedForce[i][1],distributedForce[i][2])))
#         summoment += N(integrate(x*distributedForce[i][0],(x,distributedForce[i][1],distributedForce[i][2])))
#     if support_type is 'pinjoint':
#         reaction2 = -(summoment)/float(distSupport[1]-distsupport[0])
#         reaction1 = -(sumforce) - reaction2
#         return [reaction1,reaction2]
#     if support_type is 'cantilever':
#         reaction_moment = -(summoment)
#         reaction_force = -(sumforce)
#         return [reaction_moment,reaction_force]
