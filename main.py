
# I will going to create a easy code for represents functions
# The idea is get familiar with Numpy, Panda, Mattplotlib libraries
# Starting showing sinus, cosinus and let's see what could we add...

import numpy
import matplotlib
from matplotlib import pylab, mlab, pyplot
np = numpy
plt = pyplot

from IPython.display import display
from IPython.core.pylabtools import figsize, getfigs

from pylab import *
from numpy import *
print(matplotlib.is_interactive())
matplotlib.interactive(True)
print(matplotlib.is_interactive())


###  MAIN ###


plt.ion()
fig, ax=plt.subplots()
ax.plot([1,2,3,4],[1,4,2,3])

plt.show()
plt.ioff()