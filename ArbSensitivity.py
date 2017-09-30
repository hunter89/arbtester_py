"""
Function for doing the sensitivity analysis
"""


import numpy as np
import sys
from arbwriter import writelp
from mysolver import lpsolver
import matplotlib.pyplot as plot


def arb_sens(data_vec, numscen, numsec, arb_soln, trials, rand_range):
    data = np.array(data_vec)
    outputvar = np.array(arb_soln)
    randr = rand_range

    stressed_result = np.empty((trials,numscen))
    for trial in range(trials):
        result = []
        stressed_data = np.zeros((numscen, numsec))
        for k in range(numscen):
            # Perturb scenario values of the securities except cash. Sampled from independent uniform distributions
            rad = [np.random.uniform((1 + randr)*x,(1 - randr)*x) for x in data[(k + 1)*(1 + numsec)+1:(k + 2)*(1 + numsec)]]
            stressed_data[k,:] = rad

        # The scenario value for cash is presently hard-coded with interest rate of 2%. This is appended to the stressed data
        cash_vec = (np.ones(numscen)*1.02).reshape(numscen, 1)
        stressed_data = np.hstack((cash_vec,stressed_data))
        stressed_result[trial,:] = [int(v - 0 > -0.0001) for v in np.dot(stressed_data, outputvar.reshape(numsec + 1,1))] # 0.0001 is set as tolerance

    hist_array = [sum(x) for x in stressed_result]
    return hist_array






