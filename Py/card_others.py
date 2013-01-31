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

from card import *

cols=['gray','b','red','green','gold','cyan','brown']
models=["s90_d","s91_d","pp04_d","t06_d","pp12_d","i11_d"]

# no longer needs to specify the titles explicitly,
# since they are now stored as an attribute
# of KList 

# titles=['Saltzman-Maasch 1990','Saltzman-Maasch 1991','Paillard-Parrenin 2004',
#        'Tziperman et al. 2006','Parrenin-Paillard 2012','Imbrie et al. 2011']

fig,axes = plt.subplots(nrows=2,ncols=3)
fig.set_size_inches(8.5,6)
fig.subplots_adjust(wspace=0.4, hspace=0.4, left=0.05, right=0.95)

from rpy2 import robjects
Rfile='RData/KList_others.RData'
print(robjects.r.load (Rfile))
KList = robjects.r('KList')

axes = axes.flatten()

for i,ax in enumerate(axes):
  pcard(KList[i], ax, cols)

  ax.set_xlabel("$\\tau$", fontsize=14)
  ax.set_ylabel("$\\gamma$", fontsize=14, rotation='horizontal')
  axes[i].tick_params(axis='x',direction='out')
  # needed a bit of thinking, but finally got it: 
  # extracts attribute to get consistent titile
  # without risk of error
  axes[i].set_title(robjects.r.attr(KList[i],"name")[0])
  axes[i].set_xlim((0.3,1.5))
  axes[i].set_ylim((0.05,1.4))
  axes[i].plot([1],[1], 'p', color='orange')

plt.savefig('Pdf/card_others.pdf')
