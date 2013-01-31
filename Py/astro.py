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

''' generates graphic with amplitudes of precession '''
''' and obliquity signals '''

import matplotlib.pyplot as plt
import matplotlib as mp
import numpy 

# takes amplitude, period and phase directly
# from RData. The files are directly taken from
# BER78 publication. Precession were reconstructed
# with package Insol (see documentation) 

amp_pre, phase, omega, period_pre = numpy.loadtxt('RData/precession.dat', unpack=True)
amp_obl, phase, omega, period_obl = numpy.loadtxt('RData/obliquity.dat', unpack=True)

# scales such that amplitude of first component = 1

amp_pre = abs( amp_pre / amp_pre[0] ) 
amp_obl = abs ( amp_obl / amp_obl[0] )
period_obl = period_obl / 1000. 

# two subplots 

fig, axes = plt.subplots(1,2)

# and ajusts, just as in stob.py 
fig.set_size_inches(6.3,3.4)
fig.subplots_adjust(wspace=0.2,hspace=0.2,bottom=0.15,top=.80, left=.10)

axes[0].plot(period_pre, amp_pre,'.', color='blue')
axes[1].plot(period_obl, amp_obl,'.', color='red')

axes[0].vlines(period_pre, 0, amp_pre)
axes[1].vlines(period_obl, 0, amp_obl)


axes[0].set_ylabel('amplitude ')

axes[0].set_title('Precession')
axes[1].set_title('Obliquity')

for ax in axes: 
  ax.set_xlim((0,100))
  ax.set_ylim((0,1.05))
  ax.set_xlabel('Period [ka] ')

fig.savefig('Pdf/astro.pdf')
