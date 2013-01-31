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

# illustrates convergence of pullback solutions
# as t_back increases
# code pretty self-explanatory 

import matplotlib.pyplot as plt
import matplotlib as mp
import numpy as np

mp.rcParams['figure.figsize'] =  4.2, 3.5
mp.rcParams['lines.solid_joinstyle'] =  'round'
mp.rcParams['xtick.major.width']    = 1.0
mp.rcParams['ytick.major.width']    = 1.0

T,X = np.loadtxt('RData/Ni_60.dat',unpack=True)

fig = plt.figure()
ax = fig.add_axes((0.10, 0.18, 0.8, 0.75))
ax.set_xscale('log')

# remember : 1 time unit = 10 ka
ax.plot(-T/100,X, 'p')
ax.set_xlabel('$-t_\\mathrm{back}$ [Myr]')
ax.set_title('# of distinct solutions at $t_0=0$')
ax.set_ylim((0,10))
ax.set_yticks((1,2,4,8))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.tick_params(direction='out')
fig.savefig('Pdf/convergence.pdf')

