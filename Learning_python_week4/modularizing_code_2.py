                    # Python Modules

# A module in Python is simply a file with .py extension that contains Python code (functions, variables, or classes) which can be reused in other programs.
            # Different ways to import modules
#1. Import the whole module
import math
# lets put it to use 
print(math.sqrt(9))
# Note that you must specify the module name when calling a function within it.

#2. Import as an alias
import math as m
# Lets put it to use 
print(m.sqrt(25))

#3. Import specific function or variables
from math import sqrt, pi
print(sqrt(36))
print(pi)
# - here you dont need the prefix 'math' anymore.

#4. Import everything from the module
from math import *
print(sqrt(49))
print(pi)
# - This is usually not recommended because it can cause name conflicts if two modules have function with the same name.
