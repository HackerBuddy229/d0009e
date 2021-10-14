# -*- coding: latin-1 -*-

#from io import StringIO
import sys
#import lab2
from tvarsumman import tvarsumman
from tvarsumman2 import tvarsumman2
import __main__

def testSum(fkn, printName, num, correctOutput):

  print("Testar "+printName+"("+str(num)+")...")

  sum = fkn(num)

  if sum==correctOutput:
    print("funkar!")
  else:
    print("funkar inte!")
    print("   Testresultat:  ",sum)
    print("   Rätt resultat: ",correctOutput)

testSum(tvarsumman, "tvarsumman", 123, 6)
testSum(tvarsumman, "tvarsumman", 0, 0)
testSum(tvarsumman, "tvarsumman", 7619, 23)
testSum(tvarsumman2, "tvarsumman2", 123, 6)
testSum(tvarsumman2, "tvarsumman2", 0, 0)
testSum(tvarsumman2, "tvarsumman2", 7619, 23)
