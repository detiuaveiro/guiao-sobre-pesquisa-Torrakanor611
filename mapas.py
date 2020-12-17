from constraintsearch import *

region = ['A', 'B', 'C', 'D', 'E']
colors = ['red', 'blue', 'green', 'yellow', 'white']

def mapas_constraint(r1, c1, r2, c2):
    

d = { v : colors for v in region}

c = { (X, Y):mapas_constraint for X in region for Y in region if  X != Y }


cs = ConstraintSearch(d, c)

print(cs.search())

# { A : colors
#   B : colors}

