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

# written similarly to card_periodic.py 

cols=['gray','b','red','green','gold','cyan','brown']
titles=[ 'Imbrie et al. 2011' , 'Parrenin-Paillard 2012 (*) ' ]

fig,axes = plt.subplots(1,2)
fig.subplots_adjust(wspace=0.4, hspace=0.4, bottom=0.15, top=0.9)
fig.set_size_inches(7,3.3)

from rpy2 import robjects
Rfile='RData/KList_Others_sup.RData'
print(robjects.r.load (Rfile))
KList = robjects.r('KList')

axes = axes.flatten()

for i,ax in enumerate(axes):
  print(i)
  K = KList[i]
   
  pcard(K, ax, cols)

  ax.set_xlabel("$\\tau$", fontsize=14)
  ax.set_ylabel("$\\gamma$", fontsize=14, rotation='horizontal')
  axes[i].tick_params(axis='x',direction='out')
  axes[i].set_title(titles[i])
  axes[i].plot([1],[1], 'p', color='orange')
#plt.show()

  axes[0].set_xlim(( 0.5 , 1.5 )) 
  axes[0].set_ylim(( 0, 0.15)) 
  axes[1].set_xlim(( 0.5, 1.5 )) 
  axes[1].set_ylim(( 0. , 1.5)) 

plt.savefig('Pdf/card_others_sup.pdf')
