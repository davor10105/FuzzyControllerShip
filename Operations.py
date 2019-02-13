from Fuzzy import *
from Domain import *

class Operations():
    def unaryOperation(fuzzySet,unaryFunction):
        retFuzzy=MutableFuzzySet(fuzzySet.domain)
        for element in fuzzySet.domain:
            retFuzzy.set(element,unaryFunction(fuzzySet.getValueAt(element)))
        return retFuzzy
    def binaryOperation(fuzzySetOne,fuzzySetTwo,binaryFunction):
        if fuzzySetOne.domain!=fuzzySetTwo.domain:
            raise ValueError("Operacije su definirane samo nad neizrazitim skupovima definiranim nad istom domenom")
        retFuzzy=MutableFuzzySet(fuzzySetOne.domain)
        for element in fuzzySetOne.domain:
            retFuzzy.set(element,binaryFunction(fuzzySetOne.getValueAt(element),fuzzySetTwo.getValueAt(element)))
        return retFuzzy
    def zadehNot():
        return lambda x: 1-x
    def zadehAnd():
        return lambda x,y: min(x,y)
    def zadehOr():
        return lambda x,y: max(x,y)
    def hamacherTNorm(v):
        return lambda a,b: a*b/(v+(1-v)*(a+b-a*b))
    def hamacherSNorm(v):
        return lambda a,b: (a+b-(2-v)*a*b)/(1-(1-v)*a*b)
    def product():
        return lambda x,y: x*y

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
    
    notSetOne=Operations.unaryOperation(set_one,Operations.zadehNot())
    print('notSet1:')
    print(notSetOne)

    union=Operations.binaryOperation(set_one,notSetOne,Operations.zadehOr())
    print('Set1 union notSet1:')
    print(union)

    hinters=Operations.binaryOperation(set_one,notSetOne,Operations.hamacherTNorm(1.0))
    print('Set1 intersection with notSet1 using parameterised Hamacher T norm with parameter 1.0:')
    print(hinters)
