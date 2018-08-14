from sympy import *
x = Symbol('x')
def calSupportReaction(concForce,concMoment,distributedForce,distSupport,support_type):
    sumforce = 0
    summoment = 0
    for i in range(0,len(concForce)):
        sumforce += concForce[i][0]
        summoment += concForce[i][0]*concForce[i][1]
    for i in range(0,len(concMoment)):
        summoment += concMoment[i][0]
    for i in range(0,len(distributedForce)):
        sumforce += N(integrate(distributedForce[i][0],(x,distributedForce[i][1],distributedForce[i][2])))
        summoment += N(integrate(x*distributedForce[i][0],(x,distributedForce[i][1],distributedForce[i][2])))
    if support_type is 'pinjoint':
        reaction2 = -(summoment)/float(distSupport[1]-distsupport[0])
        reaction1 = -(sumforce) - reaction2
        return [reaction1,reaction2]
    if support_type is 'cantilever':
        reaction_moment = -(summoment)
        reaction_force = -(sumforce)
        return [reaction_moment,reaction_force]

concForce =[]
concMoment = []
distributedForce = []
distSupport = []
distSupport.append(0)
distSupport.append(6)
distributedForce.append([20*x,0,6])
support_type = 'pinjoint'
reaction_forces = calSupportReaction(concForce,concMoment,distributedForce,distSupport,support_type)
print(reaction_forces)
    
    def calSupportReaction(self):
		print(self.concForce)
		print(self.concMoment)
		print(self.distributedForce)
		for i in range(0,len(self.concForce)):
			self.sumforce += self.concForce[i][0]
			
		for i in range(0,len(self.concMoment)):
			self.summoment += self.concMoment[i][0]
		for i in range(0,len(self.distributedForce)):
			self.sumforce += N(Integral(self.distributedForce[0],(self.x,self.distributedForce[i][1],self.distributedForce[i][2])))
			self.summoment += N(Integral(x*self.distributedForce[i][0],(self.x,self.distributedForce[i][1]-self.disSupport[0],self.distributedForce[i][2]-self.disSupport[0])))
		if self.supportType is 'pinjoint':
			reaction2 = (self.summoment)/(self.disSupport[1]-self.disSupport[0])
			reaction1 = sumforce - reaction2
			getDiscreteForce(self.disSupport[0],reaction1)
			getDiscreteForce(self.disSupport[1],reaction2)
		if self.supportType is 'cantilever':
			getDiscreteForce(self.disSupport[0],self.sumforce)
			getBendingMoment(self.disSupport[0],self.summonent)
