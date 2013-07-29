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

# resource package to draw 'cardinality' diagrams,
# i.e., diagrams showing the number of pullback attractors
# as a function of model parameters
# note that all the data are generated with the relevant
# 'R' programs (see R directory for more details and
# documentation

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mpl
from matplotlib import colors


def pcard(K, ax, cols, scalex=1):
  ''' main routine drawing the diagram '''
  ''' into axes '''
  ''' K  : matrix generated in R '''
  ''' ax : ax in which the diagram should be draw '''
  ''' col : array of colors, corresponding to  '''
  '''       0,1,2  etc pullback solutions '''

  x = np.array(K[K.names.index('x')])*scalex
  y = np.array(K[K.names.index('y')])
  z = np.matrix(K[K.names.index('z')]).transpose()
   
  cmap = mpl.colors.ListedColormap(cols)
  cmap.set_over('white')
  bounds=np.array(range(cols.__len__() + 1))+0.9
  norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
  extent=(x.min(),x.max(),y.min(),y.max())
  img = ax.imshow(z,extent=extent, origin='lower', 
                  cmap=cmap, norm=norm, aspect='auto')

def clegend (cols, bbox=0):
  ''' legend with cols colors '''
  ''' bbox is the bounding box coordinates '''
  ''' where the legend should be draw '''
  handles = []
  labels = []
  for i,colour in enumerate(cols):
      handles.append( plt.Rectangle((0, 0), 0.5, 1, fc=colour))
      labels.append(("%1i" % (i+1) ))

  ''' white reserved for -over the limit- attractors '''
  handles.append( plt.Rectangle((0, 0), 0.5, 1, fc='white'))
  labels.append("> %1i" % (cols.__len__() ))
  plt.figlegend(handles,labels,bbox_to_anchor=bbox, loc=3,
         ncol=2, mode="expand", borderaxespad=0.)


''' facility to draw  hash the zone of high '''
''' Rayleigh number into ax '''
''' Rayleigh number supplied as the R file where '''
''' the Rayleigh number is supposedly encoded as '''
''' matrix "KK" '''
def prayleigh (Rfile, ax):
  from rpy2 import robjects
  robjects.r.load(Rfile)
  K = robjects.r('KK')
  x = np.array(K[0])*10
  y = np.array(K[1])
  z = np.array(K[2]).transpose()
 
  cntrset = ax.contourf(x,y,z,levels=[0.95,9999], 
            colors=('black','black'), alpha=0.5, linewidth=0.01)

  # convert to hatches
  from matplotlib.patches import PathPatch

  patches_list = []
  for pathcollection in cntrset.collections:
        patches_list.append([PathPatch(p1) for p1 in  pathcollection.get_paths()])
        pathcollection.remove()

  for patches in patches_list:
    for p in patches:
      p.set_fc("None")
      p.set_ec("black")
      p.set_hatch("//////")
      ax.add_patch(p)
 
def add_second_axis(ax, shift, ratio, label, pos='bottom', dir='outward'):
  ''' add second axis below the first one '''
  ''' shift : y-shift '''
  ''' ratio : ratio between the values of this second '''
  '''         axis and the main one '''
  ''' label : x-axis label '''
  ''' position : one of top or bottom '''
  ''' dir : inward or outward direction of ticks '''

  newax = ax.twiny()
  newax.set_xlim((x * ratio  for x in ax.get_xlim()))
  newax.spines[pos].set_position(('outward', shift))
  newax.set_frame_on(True)
  newax.patch.set_visible(False)
  newax.xaxis.set_ticks_position(pos)
  newax.xaxis.set_label_position(pos)
  newax.set_xlabel(label)
  return(newax)

#plt.subplots_adjust(wspace=0,hspace=0)


