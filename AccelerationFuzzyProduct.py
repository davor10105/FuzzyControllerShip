from Domain import *
from Rule import *
from Operations import *

class AccelerationFuzzyProduct():
    def __init__(self,defuzzyfier):
        self.defuzzyfier=defuzzyfier

        self.LKDiscrete=lambda x: int(x/10)
        self.LKDomain=Domain.intRange(self.LKDiscrete(0),self.LKDiscrete(1300)+1)
        self.LK=Variable({'SMALL':CalculatedFuzzySet(self.LKDomain,StandardFuzzySets.lFunction(self.LKDomain.indexOfElement((self.LKDiscrete(30),)),self.LKDomain.indexOfElement((self.LKDiscrete(40),)))) \
                          ,'MEDIUM':CalculatedFuzzySet(self.LKDomain,StandardFuzzySets.lambdaFunction(self.LKDomain.indexOfElement((self.LKDiscrete(20),)),self.LKDomain.indexOfElement((self.LKDiscrete(130),)),self.LKDomain.indexOfElement((self.LKDiscrete(200),)))) \
                          ,'BIG':CalculatedFuzzySet(self.LKDomain,StandardFuzzySets.gammaFunction(self.LKDomain.indexOfElement((self.LKDiscrete(120),)),self.LKDomain.indexOfElement((self.LKDiscrete(220),))))},self.LKDiscrete)

        self.DKDiscrete=lambda x: int(x/10)
        self.DKDomain=Domain.intRange(self.DKDiscrete(0),self.DKDiscrete(1300)+1)
        self.DK=Variable({'SMALL':CalculatedFuzzySet(self.DKDomain,StandardFuzzySets.lFunction(self.DKDomain.indexOfElement((self.DKDiscrete(30),)),self.DKDomain.indexOfElement((self.DKDiscrete(40),)))) \
                          ,'MEDIUM':CalculatedFuzzySet(self.DKDomain,StandardFuzzySets.lambdaFunction(self.DKDomain.indexOfElement((self.DKDiscrete(20),)),self.DKDomain.indexOfElement((self.DKDiscrete(130),)),self.DKDomain.indexOfElement((self.DKDiscrete(200),)))) \
                          ,'BIG':CalculatedFuzzySet(self.DKDomain,StandardFuzzySets.gammaFunction(self.DKDomain.indexOfElement((self.DKDiscrete(120),)),self.DKDomain.indexOfElement((self.DKDiscrete(220),))))},self.DKDiscrete)

        self.VDiscrete=lambda x: min(x,100) #brzine ce se kretati od 0,100
        self.VDomain=Domain.intRange(self.VDiscrete(0),self.VDiscrete(100)+1)
        self.V=Variable({'SMALL':CalculatedFuzzySet(self.VDomain,StandardFuzzySets.lFunction(self.VDomain.indexOfElement((self.VDiscrete(15),)),self.VDomain.indexOfElement((self.VDiscrete(20),)))) \
                          ,'MEDIUM':CalculatedFuzzySet(self.VDomain,StandardFuzzySets.lambdaFunction(self.VDomain.indexOfElement((self.VDiscrete(15),)),self.VDomain.indexOfElement((self.VDiscrete(25),)),self.VDomain.indexOfElement((self.VDiscrete(35),)))) \
                          ,'BIG':CalculatedFuzzySet(self.VDomain,StandardFuzzySets.gammaFunction(self.VDomain.indexOfElement((self.VDiscrete(75),)),self.VDomain.indexOfElement((self.VDiscrete(85),))))},self.VDiscrete)

        self.ADiscrete=lambda x: max(x,-50) if x<0 else min(x,50) #akceleracije ce ici od -50,50
        self.ADomain=Domain.intRange(self.ADiscrete(-50),self.ADiscrete(50)+1)
        self.A=Variable({'NEGATIVEBIG':CalculatedFuzzySet(self.ADomain,StandardFuzzySets.lFunction(self.ADomain.indexOfElement((self.ADiscrete(-47),)),self.ADomain.indexOfElement((self.ADiscrete(-44),)))) \
                          ,'NEGATIVESMALL':CalculatedFuzzySet(self.ADomain,StandardFuzzySets.lambdaFunction(self.ADomain.indexOfElement((self.ADiscrete(-6),)),self.ADomain.indexOfElement((self.ADiscrete(-15),)),self.ADomain.indexOfElement((self.ADiscrete(0),)))) \
                         ,'ZERO':CalculatedFuzzySet(self.ADomain,StandardFuzzySets.lambdaFunction(self.ADomain.indexOfElement((self.ADiscrete(-3),)),self.ADomain.indexOfElement((self.ADiscrete(0),)),self.ADomain.indexOfElement((self.ADiscrete(3),)))) \
                         ,'POSITIVESMALL':CalculatedFuzzySet(self.ADomain,StandardFuzzySets.lambdaFunction(self.ADomain.indexOfElement((self.ADiscrete(0),)),self.ADomain.indexOfElement((self.ADiscrete(15),)),self.ADomain.indexOfElement((self.ADiscrete(6),)))) \
                          ,'POSITIVEBIG':CalculatedFuzzySet(self.ADomain,StandardFuzzySets.gammaFunction(self.ADomain.indexOfElement((self.ADiscrete(44),)),self.ADomain.indexOfElement((self.ADiscrete(47),))))},self.ADiscrete)
 

       

        self.n=Norms(Operations.zadehOr(),Operations.product())
        
    def conclude(self,L,D,LK,DK,V,S):
        method=Conclusion.Product

        #pravila
        r=[]
        
        #ako je razmak mali, ubrzaj
        r.append(Rule.conclude(self.LK.calculate('SMALL',LK),self.A.getFuzzy('POSITIVEBIG'),method))
        r.append(Rule.conclude(self.DK.calculate('SMALL',DK),self.A.getFuzzy('POSITIVEBIG'),method))
        #inace postupno ubrzavaj
        r.append(Rule.conclude(self.LK.calculate('MEDIUM',LK),self.A.getFuzzy('POSITIVESMALL'),method))
        r.append(Rule.conclude(self.DK.calculate('MEDIUM',DK),self.A.getFuzzy('POSITIVESMALL'),method))
        r.append(Rule.conclude(self.LK.calculate('BIG',LK),self.A.getFuzzy('POSITIVESMALL'),method))
        r.append(Rule.conclude(self.DK.calculate('BIG',DK),self.A.getFuzzy('POSITIVESMALL'),method))

        #ako je koridor relativno mali i brzina velika, nemoj ubrzavati
        r.append(Rule.conclude(self.n.AND(self.n.OR(self.n.AND(self.DK.calculate('SMALL',DK),self.LK.calculate('SMALL',LK)),self.n.AND(self.DK.calculate('MEDIUM',DK),self.LK.calculate('MEDIUM',LK))),self.V.calculate('BIG',V)),self.A.getFuzzy('NEGATIVEBIG'),method))
        
     
        #unija pravila
        union=r[0]
        for i in range(1,len(r)):
            union=Operations.binaryOperation(union,r[i],self.n.SNorm)

        return self.defuzzyfier(union)
