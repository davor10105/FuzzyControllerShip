class Domain():
    def intRange(a,b):
        return SimpleDomain(a,b)
    def combine(domains):
        return CompositeDomain(domains)
    def indexOfElement(self,domainElement):
        for i in range(len(self.elements)):
            if domainElement==self.elements[i]:
                return i
    def elementForIndex(self,i):
        return self.elements[i]
    def __str__(self):
        retVal=''
        k=0
        for i in self:
            k+=1
            retVal+='Element domene: '+str(i)+'\n'
        retVal+='Kardinalitet domene je: '+str(k)+'\n'
        return retVal

class SimpleDomain(Domain):
    def __init__(self,a,b):
        self.first=a
        self.last=b

        self.elements=[(i,) for i in range(a,b)]
    def getCardinality(self):
        return self.last-self.first
    def getComponent(self,i):
        return self
    def getNumberOfComponents():
        return 1
    def __iter__(self):
        return iter(self.elements)

class CompositeDomain(Domain):
    def __init__(self,simpleDomains):
        self.domains=simpleDomains
        
        self.elements=[element for element in self.domains[0]]
        for i in range(1,len(self.domains)):
            tempElements=[el for el in self.elements]
            self.elements=[]
            for element in tempElements:
                for elementTwo in self.domains[i]:
                    self.elements.append(element+elementTwo)
    def getCardinality(self):
        return len(self.elements)
    def getComponent(self,i):
        return self.domains[i]
    def getNumberOfComponents():
        return len(self.domains)
    def __iter__(self):
        return iter(self.elements)        

if __name__=='__main__':
    d1=Domain.intRange(0,5)
    print('Elementi domene d1:')
    print(d1)
    d2=Domain.intRange(0,3)
    print('Elementi domene d2:')
    print(d2)

    d3=Domain.combine([d1,d2])
    print('Elementi domene d3:')
    print(d3)

    print(d3.elementForIndex(0))
    print(d3.elementForIndex(5))
    print(d3.elementForIndex(14))
    print(d3.indexOfElement((4,1)))



