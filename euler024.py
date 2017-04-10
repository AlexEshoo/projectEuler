from sympy.utilities.iterables import multiset_permutations
import numpy as np

a = np.array([0,1,2,3,4,5,6,7,8,9])

i = 1
for p in multiset_permutations(a):
    if i == 1000000:
        print p
        break
    else:
        i += 1