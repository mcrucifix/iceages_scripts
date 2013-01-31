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
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import mpl
from matplotlib import colors
 
from rpy2 import robjects
robjects.r.load('RData/SList.RData')
SList = robjects.r('SList')

cols=('white','black')

def plot_strob(ax,X,Y,pointsize=1):
  if (pointsize==0):
    ax.plot(X,Y,'.', rasterized=False)
    ax.set_xlim((-1.5,1.5))
    ax.set_ylim((-2.5,2.5))
  else:
    ax.plot(X,Y,'.', markersize=pointsize, rasterized=True, color='black')
    ax.set_xlim((-1.5,1.5))
    ax.set_ylim((-2.5,2.5))
  return (ax)

def plot_strob_series (index,axes,toptitles=1,pointsize=(0,1,1), tau=None):
  X,Y = np.array(SList[index][0]).transpose()
  plot_strob(axes[0],X,Y,pointsize=pointsize[0])
  if (tau != None):
    bbox_args = dict(boxstyle="square", fc='white')
    axes[0].text(-3.5, 0, "$\\tau$=%2.0f ka"%tau, 
            clip_on = False, rotation=0, bbox=bbox_args,
            verticalalignment='center')


  X,Y,d1,d2 = np.array(SList[index][1]).transpose()
  plot_strob(axes[1],X,Y,pointsize=pointsize[1])

  if (len(pointsize) > 2):
    X,Y,d1,d2 = np.array(SList[index][2]).transpose()
    plot_strob(axes[2],X,Y,pointsize=pointsize[2])

  if (toptitles):
    axes[0].set_title('Pullback section')
    axes[1].set_title('Stroboscopic on $P_1$')
    if (len(pointsize) > 2):
      axes[2].set_title('Stroboscopic on $O_1$')

matplotlib.rcParams.update({'font.size': 10})

def preparefig(nrows,ncols, height, width):
  plt.clf()
  fig,axes = plt.subplots(nrows, ncols)
  fig.set_size_inches(height,width)
  fig.subplots_adjust(wspace=0.2,hspace=0.2,bottom=0.10,top=.90, left=.18)

  for ax in axes.flatten():
    ax.xaxis.set_major_formatter( plt.NullFormatter() )
    ax.yaxis.set_major_formatter( plt.NullFormatter() )
    ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))
    ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
  return(fig,axes)

def finishfig(axes):
  for ax in axes[:,0]:
    ax.yaxis.set_major_formatter (plt.FormatStrFormatter("%2.0f"))

  for ax in axes[-1,:]:
    ax.xaxis.set_major_formatter (plt.FormatStrFormatter("%2.0f"))


fig,axes = preparefig(1,2,6.3,3.4) 

# slightly modify the subplots presentation, for this particular
# figure with only two panels:

fig.subplots_adjust(wspace=0.2,hspace=0.2,bottom=0.15,top=.80, left=.10)

# reshape for convenience in the following of the code. Won't alter
# the col / row presentation 

axes = axes.reshape(1,2)
plot_strob_series (0,axes[0,:],toptitles=1,pointsize=(0,2), tau=None)
axes[0,0].set_xlabel("x")
axes[0,0].set_ylabel("y")
axes[0,1].set_xlabel("x")
finishfig(axes)
fig.suptitle('Periodic forcing ($P_1$)', fontproperties=fm.FontProperties(size="large"))
fig.savefig('Pdf/strob_periodic.pdf', rasterized=False)


fig,axes = preparefig(3,3,6.7,6)
plot_strob_series (1,axes[0,:],toptitles=1,pointsize=(0,1,1), tau=36)
plot_strob_series (2,axes[1,:],toptitles=0,pointsize=(0,1,1), tau=41)
plot_strob_series (3,axes[2,:],toptitles=0,pointsize=(0,1,1), tau=44)
finishfig(axes)
fig.suptitle('Quasi-periodic forcing ($P_1 + E_1$)')
fig.savefig('Pdf/strob_2periods.pdf', dpi=1000, rasterized=False)







