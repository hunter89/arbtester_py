
from ArbTester import *
from ArbSensitivity import *
import matplotlib.pyplot as plot


datafile, lpfile = "little.dat","lpfile.lp"

# Check Arbitrage
data,nscen, nsec, arb_soln = arb_tester(datafile, lpfile)

# Perform Sensitivity
sens_output = arb_sens(data, nscen, nsec, arb_soln, 100, 0.05)    # arguments include number of trails and percentage for perturbing the data
print (sens_output)

# Print histogram
bins = list(range(1,nscen + 1,1))
hist_data, bins =  np.histogram(sens_output,bins)
width = 0.8 * (bins[1] - bins[0])
plot.bar(bins[:-1], hist_data, align='center', width=width)
plot.xlabel('Scenario score (sum)')
plot.ylabel('Frequency')
plot.show()