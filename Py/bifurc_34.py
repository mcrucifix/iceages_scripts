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

'''mostly written like bifurc_11.py'''

from rpy2 import robjects
print(robjects.r.load ('../RData/LB_34_34_Gamma20_fast.RData'))
LB = robjects.r('LB')
 
Omegas = np.array(robjects.r('Omegas'))*10.

fig,axes = plt.subplots(2,1)

for i,L in enumerate(LB):
  for j,S in enumerate(L):
    for k in range(2): 
      M = np.matrix(S).transpose()
      axes[k].scatter (Omegas[i],M[k,0],marker=',',edgecolors='None',s=2., color='b')
      for x in [36,41,44]: axes[k].axvline(x,linestyle='--', color='gray')

for ax in axes: ax.set_xlim((Omegas.min(), Omegas.max()))

axes[0].set_ylabel("x")
axes[1].set_ylabel("y")
axes[1].set_xlabel("$\\tau$ [ka]")
fig.set_size_inches(6,6)
fig.suptitle("Pullback sections at t=0Ma \n Full astronomical forcing")
fig.savefig('bifurc_34_tau_2_fast.pdf')
