from Variable import *
from Fuzzy import *

class Norms():
    def __init__(self,SNorm,TNorm):
        self.SNorm=SNorm
        self.TNorm=TNorm
    def AND(self,x,y):
        return self.TNorm(x,y)
    def OR(self,x,y):
        return self.SNorm(x,y)

class Conclusion():
    def Mamdani(antecedent,consequence):
        retVal=MutableFuzzySet(consequence.domain)
        for element in consequence.domain:
            retVal.set(element,min(antecedent,consequence.getValueAt(element)))
        #print(retVal)
        return retVal
    def Product(antecedent,consequence):
        retVal=MutableFuzzySet(consequence.domain)
        for element in consequence.domain:
            retVal.set(element,antecedent*consequence.getValueAt(element))
        return retVal

class Rule():
    def conclude(antecedent,consequence,conclusionMethod):
        return conclusionMethod(antecedent,consequence)


