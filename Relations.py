from Domain import *
from Fuzzy import *
from Operations import *

class Relations():
    def isUtimesURelation(relation):
        if len(relation.domain.elements[0])!=2:
            return False
        x=set()
        y=set()
        for element in relation.domain:
            x.add(element[0])
            y.add(element[1])
        if x!=y:
            return False
        return True
    def isSymmetric(relation):
        if Relations.isUtimesURelation(relation)==False:
            return False
        checked=dict()
        for element in relation.domain:
            try:
                checked[element]
                continue
            except:
                pass
            if relation.getValueAt(element)!=relation.getValueAt((element[1],element[0])):
                return False
            checked[element]=True
            checked[(element[1],element[0])]=True
        return True
    def isReflexive(relation):
        if Relations.isUtimesURelation(relation)==False:
            return False
        for element in relation.domain:
            if element[0]==element[1]:
                if relation.getValueAt(element)!=1:
                    return False
        return True
    def isMaxMinTransitive(relation):
        if Relations.isUtimesURelation(relation)==False:
            return False
        for element in relation.domain:
            for elementTwo in relation.domain:
                if elementTwo==element:
                    continue
                if element[0]==elementTwo[0]:
                    y=elementTwo[1]

                    if relation.getValueAt(element)<min(relation.getValueAt((element[0],y)),relation.getValueAt((y,element[1]))):
                        return False
        return True
    def compositionOfBinaryRelations(r1,r2):
        u=r1.domain.domains[0]
        w=r2.domain.domains[1]
        uw=Domain.combine([u,w])
        newFuzzy=MutableFuzzySet(uw)
        for element in r1.domain:
            for elementTwo in r2.domain:
                if element[1]!=elementTwo[0]:
                    continue
                newFuzzy.set((element[0],elementTwo[1]),max(min(r1.getValueAt(element),r2.getValueAt(elementTwo)),newFuzzy.getValueAt((element[0],elementTwo[1]))))
        return newFuzzy
    def isFuzzyEquivalence(relation):
        return Relations.isReflexive(relation) and Relations.isSymmetric(relation) and Relations.isMaxMinTransitive(relation)

                
        

u=Domain.intRange(1,6)
u2=Domain.combine([u,u])

r1=MutableFuzzySet(u2)
r1.set((1,1),1)
r1.set((2,2),1)
r1.set((3,3),1)
r1.set((4,4),1)
r1.set((5,5),1)
r1.set((3,1),0.5)
r1.set((1,3),0.5)

r2=MutableFuzzySet(u2)
r2.set((1,1),1)
r2.set((2,2),1)
r2.set((3,3),1)
r2.set((4,4),1)
r2.set((5,5),1)
r2.set((3,1),0.5)
r2.set((1,3),0.1)

r3=MutableFuzzySet(u2)
r3.set((1,1),1)
r3.set((2,2),1)
r3.set((3,3),0.3)
r3.set((4,4),1)
r3.set((5,5),1)
r3.set((1,2),0.6)
r3.set((2,1),0.6)
r3.set((2,3),0.7)
r3.set((3,2),0.7)
r3.set((3,1),0.5)
r3.set((1,3),0.5)

r4=MutableFuzzySet(u2)
r4.set((1,1),1)
r4.set((2,2),1)
r4.set((3,3),1)
r4.set((4,4),1)
r4.set((5,5),1)
r4.set((1,2),0.4)
r4.set((2,1),0.4)
r4.set((2,3),0.5)
r4.set((3,2),0.5)
r4.set((3,1),0.4)
r4.set((1,3),0.4)

print('r1 je definiran nad UxU? '+str(Relations.isUtimesURelation(r1)))
print('r1 je simetricna? '+str(Relations.isSymmetric(r1)))
print('r2 je simetricna? '+str(Relations.isSymmetric(r2)))
print('r1 je refleksivna? '+str(Relations.isReflexive(r1)))
print('r3 je refleksivna? '+str(Relations.isReflexive(r3)))
print('r3 je max-min tranzitivna? '+str(Relations.isMaxMinTransitive(r3)))
print('r4 je max-min tranzitivna? '+str(Relations.isMaxMinTransitive(r4)))
print()

u1=Domain.intRange(1,5)
u2=Domain.intRange(1,4)
u3=Domain.intRange(1,5)

r1=MutableFuzzySet(Domain.combine([u1,u2]))
r1.set((1,1),0.3)
r1.set((1,2),1)
r1.set((3,3),0.5)
r1.set((4,3),0.5)

r2=MutableFuzzySet(Domain.combine([u2,u3]))
r2.set((1,1),1)
r2.set((2,1),0.5)
r2.set((2,2),0.7)
r2.set((3,3),1)
r2.set((3,4),0.4)

r1r2=Relations.compositionOfBinaryRelations(r1,r2)
print(r1r2)

u=Domain.intRange(1,5)
r=MutableFuzzySet(Domain.combine([u,u]))
r.set((1,1),1)
r.set((2,2),1)
r.set((3,3),1)
r.set((4,4),1)
r.set((1,2),0.3)
r.set((2,1),0.3)
r.set((2,3),0.5)
r.set((3,2),0.5)
r.set((3,4),0.2)
r.set((4,3),0.2)

r2=r
print('Pocetna relacija je neizrazita relacija ekvivalencije? '+str(Relations.isFuzzyEquivalence(r2)))
for i in range(3):
    r2=Relations.compositionOfBinaryRelations(r2,r)
    print('Broj odradenih kompozicija: '+str(i+1)+'. Relacija je:')
    print(r2)
    print('Ova relacija je neizrazita relacija ekvivalencije? '+str(Relations.isFuzzyEquivalence(r2)))
    print()

