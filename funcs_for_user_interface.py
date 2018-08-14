def getValuesForNewBeam(builder,pinjoint,cantilever):
	resultantDictionary={}
	resultantDictionary['Length']=float(builder.get_object('Length_of_Beam').get_text())
	resultantDictionary['E']=float(builder.get_object('Youngs_Modulus').get_text())
	if(pinjoint):
		resultantDictionary['Support-Type']='pin joint'
	else:
		resultantDictionary['Support-Type']='cantilever'
	builder.get_object('Length_of_Beam').set_text('Value Set')
	builder.get_object('Youngs_Modulus').set_text('Value Set')
	return resultantDictionary
def getValuesForDiscreteForce(builder):
	resultantDictionary={}
	resultantDictionary['Distance']=float(builder.get_object('Distance_Of_Discrete_Force').get_text())
	print(builder.get_object('Distance_Of_Discrete_Force').get_text())
	resultantDictionary['Magnitude']=float(builder.get_object('Magnitude_Of_Discrete_Force').get_text())
	print(builder.get_object('Magnitude_Of_Discrete_Force').get_text())
	builder.get_object('Distance_Of_Discrete_Force').set_text('')
	builder.get_object('Magnitude_Of_Discrete_Force').set_text('')
	return resultantDictionary

def getValuesForContinuousForce(builder):
	resultantDictionary={}
	resultantDictionary['Left Distance']=float(builder.get_object('Start_Of_Continuous_Force').get_text())
	print(builder.get_object('Start_Of_Continuous_Force').get_text())
	resultantDictionary['Right Distance']=float(builder.get_object('End_Of_Continuous_Force').get_text())
	print(resultantDictionary['Right Distance'])
	resultantDictionary['Equation']=builder.get_object('Equation_Of_Continuous_Force').get_text()
	print(resultantDictionary['Equation'])
	builder.get_object('Start_Of_Continuous_Force').set_text('')
	builder.get_object('End_Of_Continuous_Force').set_text('')
	builder.get_object('Equation_Of_Continuous_Force').set_text('')
	return resultantDictionary
def getValuesForMoment(builder):
	resultantDictionary={}
	resultantDictionary['Distance']=float(builder.get_object('Distance_Of_Moment').get_text())
	print(builder.get_object('Distance_Of_Discrete_Force').get_text())
	resultantDictionary['Magnitude']=float(builder.get_object('Magnitude_Of_Moment').get_text())
	print(builder.get_object('Magnitude_Of_Discrete_Force').get_text())
	builder.get_object('Distance_Of_Moment').set_text('')
	builder.get_object('Magnitude_Of_Moment').set_text('')
	return resultantDictionary