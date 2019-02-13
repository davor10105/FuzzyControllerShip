from Domain import *

#Domain.intRange,{'SMALL':CalculatedFuzzySet(domain,StandardFuzzySets.lambdaFunction(Domain.intRange)}

class Variable():
    def __init__(self,variableDict,discrete):
        self.variableDict=variableDict
        self.discrete=discrete
    def calculate(self,name,x):
        #print(self.variableDict[name].getValueAt((self.discrete(x),)))
        return self.variableDict[name].getValueAt((self.discrete(x),))
    def getFuzzy(self,name):
        return self.variableDict[name]
            
