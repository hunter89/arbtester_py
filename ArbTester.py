"""
The function is modified slightly to return data vector, number of scenarios/securities, output variable values of optimization
"""


import numpy as np
import sys
from arbwriter import writelp
from mysolver import lpsolver

def arb_tester(data_file, lp_file ):

    args = [data_file, lp_file]

    datafile = open(args[0], 'r')

    lines = datafile.readlines();
    datafile.close()

    # print lines[0]
    firstline = lines[0].split()
    # print "first line is", firstline

    numsec = int(firstline[1])
    numscen = int(firstline[3])
    r = float(firstline[5])
    print("\n")
    print("number of securities:", numsec, "number of scenarios", numscen, "r", r)
    print("\n")

    # allocate prices as one-dim array
    p = [0] * (1 + numsec) * (1 + numscen)
    k = 0
    # line k+1 has scenario k (0 = today)
    while k <= numscen:
        thisline = lines[k + 1].split()
        #    print "line number", k+1,"is", thisline
        # should check that the line contains numsec + 1 words
        j = 1
        #    print "scenario", k,":"
        p[k * (1 + numsec)] = 1 + r * (k != 0)
        while j <= numsec:
            value = float(thisline[j])
            p[k * (1 + numsec) + j] = value
            #        print " sec ", j, " -> ", p[k*(1 + numsec) + j]
            j += 1
        k += 1
#    print(p)

    # now write LP file, now done in a separate function (should read data this way, as well)

    lpwritecode = writelp(args[1], p, numsec, numscen)

    print("wrote LP to file", args[1], "with code", lpwritecode)

    # now solve lp

    outputvar = np.array(lpsolver(args[1], "test.log"))

    return p, numscen, numsec,outputvar
