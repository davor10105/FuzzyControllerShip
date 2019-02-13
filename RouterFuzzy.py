from Domain import *
from Rule import *
from Operations import *

class RouterFuzzy():
    def __init__(self,defuzzyfier):
        self.defuzzyfier=defuzzyfier

        self.LKDiscrete=lambda x: int(x/10)
        self.LKDomain=Domain.intRange(self.LKDiscrete(0),self.LKDiscrete(1300)+1)
        self.LK=Variable({'SMALL':CalculatedFuzzySet(self.LKDomain,StandardFuzzySets.lFunction(self.LKDomain.indexOfElement((self.LKDiscrete(30),)),self.LKDomain.indexOfElement((self.LKDiscrete(70),)))) \
                          ,'MEDIUM':CalculatedFuzzySet(self.LKDomain,StandardFuzzySets.lambdaFunction(self.LKDomain.indexOfElement((self.LKDiscrete(50),)),self.LKDomain.indexOfElement((self.LKDiscrete(100),)),self.LKDomain.indexOfElement((self.LKDiscrete(400),)))) \
                          ,'BIG':CalculatedFuzzySet(self.LKDomain,StandardFuzzySets.gammaFunction(self.LKDomain.indexOfElement((self.LKDiscrete(120),)),self.LKDomain.indexOfElement((self.LKDiscrete(220),))))},self.LKDiscrete)

        self.DKDiscrete=lambda x: int(x/10)
        self.DKDomain=Domain.intRange(self.DKDiscrete(0),self.DKDiscrete(1300)+1)
        self.DK=Variable({'SMALL':CalculatedFuzzySet(self.DKDomain,StandardFuzzySets.lFunction(self.DKDomain.indexOfElement((self.DKDiscrete(30),)),self.DKDomain.indexOfElement((self.DKDiscrete(70),)))) \
                          ,'MEDIUM':CalculatedFuzzySet(self.DKDomain,StandardFuzzySets.lambdaFunction(self.DKDomain.indexOfElement((self.DKDiscrete(50),)),self.DKDomain.indexOfElement((self.DKDiscrete(100),)),self.DKDomain.indexOfElement((self.DKDiscrete(400),)))) \
                          ,'BIG':CalculatedFuzzySet(self.DKDomain,StandardFuzzySets.gammaFunction(self.DKDomain.indexOfElement((self.DKDiscrete(120),)),self.DKDomain.indexOfElement((self.DKDiscrete(220),))))},self.DKDiscrete)
 

        self.KDiscrete=lambda x: max(x,-90) if x<0 else min(x,90) #akceleracije ce ici od -10,10
        self.KDomain=Domain.intRange(self.KDiscrete(-90),self.KDiscrete(90)+1)
        self.K=Variable({'NEGATIVEBIG':CalculatedFuzzySet(self.KDomain,StandardFuzzySets.lFunction(self.KDomain.indexOfElement((self.KDiscrete(-80),)),self.KDomain.indexOfElement((self.KDiscrete(-70),)))) \
                          ,'NEGATIVESMALL':CalculatedFuzzySet(self.KDomain,StandardFuzzySets.lambdaFunction(self.KDomain.indexOfElement((self.KDiscrete(-20),)),self.KDomain.indexOfElement((self.KDiscrete(-15),)),self.KDomain.indexOfElement((self.KDiscrete(0),)))) \
                         ,'ZERO':CalculatedFuzzySet(self.KDomain,StandardFuzzySets.lambdaFunction(self.KDomain.indexOfElement((self.KDiscrete(-50),)),self.KDomain.indexOfElement((self.KDiscrete(0),)),self.KDomain.indexOfElement((self.KDiscrete(5),)))) \
                         ,'POSITIVESMALL':CalculatedFuzzySet(self.KDomain,StandardFuzzySets.lambdaFunction(self.KDomain.indexOfElement((self.KDiscrete(0),)),self.KDomain.indexOfElement((self.KDiscrete(15),)),self.KDomain.indexOfElement((self.KDiscrete(20),)))) \
                          ,'POSITIVEBIG':CalculatedFuzzySet(self.KDomain,StandardFuzzySets.gammaFunction(self.KDomain.indexOfElement((self.KDiscrete(70),)),self.KDomain.indexOfElement((self.KDiscrete(80),))))},self.KDiscrete)


        self.n=Norms(Operations.zadehOr(),Operations.zadehAnd())
        
    def conclude(self,L,D,LK,DK,V,S):
        method=Conclusion.Mamdani

        #pravila
        r=[]
        #LK je mali, motaj jako desno
        r.append(Rule.conclude(self.n.AND(self.LK.calculate('SMALL',LK),self.n.OR(self.DK.calculate('MEDIUM',DK),self.DK.calculate('BIG',DK))),self.K.getFuzzy('NEGATIVEBIG'),method))
        #DK je mali, motaj jako lijevo
        r.append(Rule.conclude(self.n.AND(self.DK.calculate('SMALL',DK),self.n.OR(self.LK.calculate('MEDIUM',LK),self.LK.calculate('BIG',LK))),self.K.getFuzzy('POSITIVEBIG'),method))

        r.append(Rule.conclude(self.n.AND(self.LK.calculate('MEDIUM',LK),self.DK.calculate('BIG',DK)),self.K.getFuzzy('NEGATIVESMALL'),method))
        #DK je mali, motaj jako lijevo
        r.append(Rule.conclude(self.n.AND(self.DK.calculate('MEDIUM',DK),self.LK.calculate('BIG',LK)),self.K.getFuzzy('POSITIVESMALL'),method))


        #unija pravila
        union=r[0]
        for i in range(1,len(r)):
            union=Operations.binaryOperation(union,r[i],self.n.SNorm)

        return self.defuzzyfier(union)
