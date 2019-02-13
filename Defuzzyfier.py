class Defuzzyfier():
    def COA(fuzzySet):
        sumaMiX=0
        sumaMi=0
        for element in fuzzySet.domain:
            mi=fuzzySet.getValueAt(element)
            sumaMiX+=element[0]*mi
            sumaMi+=mi
        if sumaMi==0:
            return 0
        return int(sumaMiX/sumaMi)
