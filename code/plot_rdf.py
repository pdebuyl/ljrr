import numpy as np
import matplotlib.pyplot as plt

import sys
import os.path

plt.rcParams['figure.figsize']= (6,3.6)
plt.rcParams['font.size'] = 18
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['figure.subplot.left'] = 0.15
plt.rcParams['figure.subplot.bottom'] = 0.2

for data in sys.argv[2:]:
    x, rdf = np.loadtxt(data, unpack=True)
    rho = float(os.path.basename(data).split('_')[1])
    plt.plot(x, rdf/rho)

plt.xlim(0,3.5)
plt.xlabel(r'$r$')
plt.ylabel(r'$g(r)$')
plt.savefig(sys.argv[1])
