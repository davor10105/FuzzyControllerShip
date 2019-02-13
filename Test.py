import sys
from AccelerationFuzzyTest import *
from Defuzzyfier import *

acceleration=AccelerationFuzzy(Defuzzyfier.COA)

str = input()
(L,D,LK,DK,V,S) = [int(s) for s in str.split(" ") if s.isdigit()]

#print(L,D,LK,DK,V,S)

akcel = acceleration.conclude(L,D,LK,DK,V,S,0,True)

sys.stdout.flush()
