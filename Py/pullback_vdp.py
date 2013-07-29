# Copyright (c) 2012 Michel Crucifix <michel.crucifix@uclouvain.be>

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject

# the following conditions:

# The above copyright notice and this permission notice shall be
# incluuded in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND INFRINGEMENT
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR

# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# ------------------------------------------------------------------
# Code developed for Python 2.7 
# ------------------------------------------------------------------ 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mpl
from matplotlib import colors
import itertools

from rpy2 import robjects
file='pullback_34'


fig,ax = plt.subplots(nrows=3,ncols=1)
fig.subplots_adjust( hspace=0.6) 
fig.set_size_inches(7,7)

print(robjects.r.load ('../RData/'+file+'.RData'))
p41 = robjects.r('p41')
s41 = robjects.r('s41')
p40 = robjects.r('p40')
times = np.array(robjects.r('times'))*10.

clr = itertools.cycle(('red','green'))

for Y in p41:
  Y = np.array(Y)[:,0]
  c = clr.next();
  ax[0].plot(times,Y, linewidth=1.2, color=c)
  ax[1].plot(times,Y,'-', linewidth=0.5, color=c)
  ax[2].plot(times,Y,'-', linewidth=0.5, color=c)

ax[2].plot(times,np.array(s41)[:,0], linewidth=1.2, color='black')
ax[1].plot(times,np.array(p40)[:,0], linewidth=1.2, color='black')

ax[0].set_title('pullback attractors $\\tau=41\,\\mathrm{ka}$')
ax[2].set_title('one stochastic realisation  $\\tau=41\,\\mathrm{ka}$')
ax[1].set_title('one pullback attractor $\\tau=40\,\\mathrm{ka}$')

for j in range(3):
  ax[j].xaxis.set_major_locator(plt.MaxNLocator(4))
  ax[j].xaxis.set_major_locator(plt.MaxNLocator(4))
  ax[j].set_xticks(np.arange(0,2000,200))
  ax[j].set_ylabel('y')

ax[2].set_xlabel('time [kyr]')

fig.savefig('../Pdf/pullback_vdp_34.pdf')



