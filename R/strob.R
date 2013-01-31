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
# R version 2.15.2 (2012-10-26) -- "Trick or Treat"
# ------------------------------------------------------------------ 

require(iceages)
data(models)

# we are going for an ambitious stroboscopic plot
# with no less that 50 000 points, 
# initial conditions are the pullback attractor
# estimated by going back to -500 * 10ka = -5 Ma.

N= 50000.
tback = -500

# we retain only the first component of precession and obliquity
Astro <- read_astro(1,1)

# ... and get the periods directly from the tabe
DTOBL = 2*pi/Astro$omeobl[1]
DTPRE = 2*pi/Astro$omepre[1]

SList = list()
model = models$vdp_d
par = c(alpha=30, beta=0.7, gammapre=0.6, gammaobl=0.6, omega=3.6, asym=0.)

# ready for the three experiments. The code is pretty self-explanatory
Astro <- read_astro(1,0)
PB = basin(model, par, tback, 0, Astro)$clusters
SP = propagate_d(model, times=seq(N)*DTPRE, PB[1, ], par, Astro)
SO = propagate_d(model, times=seq(N)*DTOBL, PB[1, ],par, Astro)
SList = append(SList, list(list(PB,SP,SO)))

Astro <- read_astro(1,1)
PB = basin(model, par, tback, 0, Astro)$clusters
SP = propagate_d(model, times=seq(N)*DTPRE, PB[1, ], par, Astro)
SO = propagate_d(model, times=seq(N)*DTOBL, PB[1, ],par, Astro)
SList = append(SList, list(list(PB,SP,SO)))

par['omega'] = 4.1
PB = basin(model, par, tback, 0, Astro)$clusters
SP = propagate_d(model, times=seq(N)*DTPRE, PB[1, ], par, Astro)
SO = propagate_d(model, times=seq(N)*DTOBL, PB[1, ], par, Astro)
SList = append(SList, list(list(PB,SP,SO)))

par['omega'] = 4.4
PB = basin(model, par, tback, 0, Astro)$clusters
SP = propagate_d(model, times=seq(N)*DTPRE, PB[1, ], par, Astro)
SO = propagate_d(model, times=seq(N)*DTOBL, PB[1, ], par, Astro)
SList = append(SList, list(list(PB,SP,SO)))

save(SList, file='../RData/SList.RData')
