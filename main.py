
# I will going to create a easy code for represents functions
# The idea is get familiar with Numpy, Panda, Mattplotlib libraries
# Starting showing sinus, cosinus and let's see what could we add...

import numpy as np
import matplotlib.pyplot as plt



###  MAIN ###

x = np.arange(-2*np.pi,2*np.pi,0.1)

y = np.sin(x)
z = np.cos(x)

## TWO SUBPLOTS
fig, (ax1, ax2) = plt.subplots(1,2)
ax1.plot(x,y)
ax2.plot(x,z)
plt.show()

## SAME PLOT
fig, ax = plt.subplots()
ax.plot(x,y, label="sin")
ax.plot(x,z,label="cos")
plt.title("SIN & COS")
plt.legend()

plt.show()