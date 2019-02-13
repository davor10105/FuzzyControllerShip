import sys
from AccelerationFuzzy import *
from AccelerationFuzzyProduct import *
from RouterFuzzy import *
from RouterFuzzyProduct import *
from Defuzzyfier import *

router=RouterFuzzyProduct(Defuzzyfier.COA)
acceleration=AccelerationFuzzyProduct(Defuzzyfier.COA)

while True:
    str = input()
    (L,D,LK,DK,V,S) = [int(s) for s in str.split(" ") if s.isdigit()]

    #print(L,D,LK,DK,V,S)
    
    akcel = acceleration.conclude(L,D,LK,DK,V,S)
    kormilo = router.conclude(L,D,LK,DK,V,S)
    print(akcel, kormilo)
    sys.stdout.flush()
