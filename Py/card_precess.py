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

cols=('gray','b','red','green','gold','cyan','brown')

fig = plt.figure()
fig.set_size_inches(7,6)
ax = fig.add_axes((0.1, 0.3, 0.8, 0.55))

from rpy2 import robjects
Rfile='../RData/Card_vdp.RData'
print(robjects.r.load (Rfile))
KList = robjects.r('KList')
K = KList[2]
 
pcard(K, ax, cols)
ax.set_xlabel("$\\tau$", fontsize=18)
ax.set_ylabel("$\\gamma$", fontsize=18, rotation='horizontal')
ax.set_xlim((0.7, 5.))
fig.suptitle("2-period forcing ($P_2$ and $P_3$)")
ax.tick_params(axis='x',direction='out')

add_second_axis(ax, 40, 2.7436 / 2.242800 , "$P_N / P_2$")
add_second_axis(ax, 80, 2.7436 / 1.897600 , "$P_N / P_3$")
add_second_axis(ax, 10, 2.7436 / 12.32970 , "$P_N / E_3$", pos='top', dir='inward' )

#clegend(cols, bbox=(0.10, 0.70, .3, .402))

prayleigh('../RData/Ray.RData', ax)

plt.savefig('card_precess.pdf')
