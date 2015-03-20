__author__ = 'Bersik'
import re
pp=re.search("\(([^()]*)\)","(fgh )f (dfg )")
if pp != None:
    print pp.group()
else:
    print "None"
