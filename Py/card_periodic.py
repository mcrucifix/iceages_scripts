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
ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))

from rpy2 import robjects
Rfile='Klist_vdp.RData'
print(robjects.r.load (Rfile))
K = robjects.r('KList[["periodic"]]')
 
pcard(K, ax, cols)
ax.set_xlabel("$\\tau$", fontsize=18)
ax.set_ylabel("$\\gamma$", fontsize=18, rotation='horizontal')
ax.set_title("Periodic forcing ($P_1$)")
ax.tick_params(axis='x',direction='out')
add_second_axis(ax, 40, 1.156852, "$P_N / P_1$")
clegend(cols, bbox=(0.10, 0.70, .3, .402))


#plt.show()
plt.savefig('card_periodic.pdf')
