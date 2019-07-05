#!/usr/bin/python
#< ----------- Starts the ManipuLogic program up ----------- >

""" Program-level TODOs:
    1.) Check all comments for clarity
    2.) Create CLI interation
    3.) Create GUI interaction
    4.) Refactor such that classes, functions, data, and control flow
        are abstracted away to account for 1st order logic.
"""

import sys
sys.path.append('Classes')
from Propositions import *



def pr():
    print("CP " + ~cp)
    print("")

p = SimpleProp("Socrates is a man.")
q = SimpleProp("2 + 2 = 5")
cp = -p
pr()
cp = -cp
pr()

cp = -(p > q)
pr()

cp = -(p + q)
pr()
print(p == p)
print (p == cp)


