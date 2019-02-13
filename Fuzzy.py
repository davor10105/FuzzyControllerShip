from Domain import *

class CalculatedFuzzySet():
    def __init__(self,domain,unaryFunction):
        self.domain=domain
        self.function=unaryFunction
    def getValueAt(self,element):
        return self.function(self.domain.indexOfElement(element))
    def __str__(self):
        retVal=''
        for element in self.domain:
            retVal+='d('+str(element)+')='+str(round(self.getValueAt(element),6))+'\n'
        return retVal

class MutableFuzzySet():
    def __init__(self,domain):
        self.domain=domain
        self.memberships=dict()
        for element in self.domain.elements:
            self.memberships[element]=0
    def set(self,element,value):
        self.memberships[element]=value
        return self
    def getValueAt(self,element):
        return self.memberships[element]
    def __str__(self):
        retVal=''
        for key,value in self.memberships.items():
            retVal+='d('+str(key)+')='+str(round(value,6))+'\n'
        return retVal
        
class StandardFuzzySets():
    def lFunction(a,b):
        return lambda x: 1 if x<a else float(b-x)/(b-a) if x<b else 0
    def gammaFunction(a,b):
        return lambda x: 0 if x<a else float(x-a)/(b-a) if x<b else 1
    def lambdaFunction(a,b,c):
        return lambda x: 0 if x<a else float(x-a)/(b-a) if x<b else float(c-x)/(c-b) if x<c else 0


if __name__=='__main__':
    d=Domain.intRange(0,11)
    set_one=MutableFuzzySet(d)
    set_one.set((0,),1.0)
    set_one.set((1,),0.8)
    set_one.set((2,),0.6)
    set_one.set((3,),0.4)
    set_one.set((4,),0.2)

    print('Set1:')
    print(set_one)

    d_two=Domain.intRange(-5,6)
    set_two=CalculatedFuzzySet(d_two,StandardFuzzySets.lambdaFunction(d_two.indexOfElement((-4,)),d_two.indexOfElement((0,)),d_two.indexOfElement((4,))))

    print('Set2:')
    print(set_two)
        
        
