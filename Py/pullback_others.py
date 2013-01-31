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
  
from rpy2 import robjects


names = ('pp04','pp12','t06','i11','s91','s90')
factors = (1,1,1,-1,1,1)

fig,ax = plt.subplots(nrows=6,ncols=1)
fig.set_size_inches(5,5)
N = names.__len__()
Rfile='RData/pullback_others.RData'
print(robjects.r.load (Rfile))
PULL = robjects.r('PULL')

for j,name,factor in zip(range(N), names, factors) :
  # sounds silly : must be an other way of doing it
  K = PULL[next(i for i, v in enumerate(PULL.names) if v == name)]
  S = K[1]
  N = S.__len__()

  times = np.arange(-800,1,1)

  for  i in range(N):
    Y = np.matrix(S[i])[:,0]*factor
    ax[j].plot(times,Y,'-')


  ax[j].set_ylabel(name.upper())
  ax[j].yaxis.set_major_locator(plt.MaxNLocator(4))

for j in range(5): ax[j].set_xticklabels([])
ax[5].set_xlabel('time (kyr)')

fig.savefig('Pdf/pullback_others.pdf')



