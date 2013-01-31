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

# pullback attractors of vanderpol oscillator
# driven by periodic ersatz of precession and obliquity
# with standard parameters 

Astro <- read_astro(1,1)
times=seq(0,200,0.5)

# determinstic parameter set
parvdp  = c(alpha=30.0, beta=0.7,  gammapre=0.6, gammaobl=0.6,
            omega=4.10, asym=0)

# stochastic parameter set
parvdps = c(alpha=30.0, beta=0.7,  gammapre=0.6, gammaobl=0.6, 
            omega=4.10, sigma=0.5)

# initial conditions positioned on the pullback attractor at time 0
# we do this rather than using the convenient 'pullaback_d' because
# we want to be able to restart from the same IC with the stochastic model

init <- basin(models$vdp_d, par=parvdp, -500., 0, Astro=Astro)$clusters

p41 <- list()
for (i in seq(nrow(init)))
 {
  p41[[i]] <- propagate_d(models$vdp_d, times, init=init[i,], par=parvdp, Astro=Astro)
 }

# tweaks the paramer 
parvdp40 = parvdp
parvdp40['omega'] = 4.0


# generates the 'stochastic' and 'deterministic' tweaked attractors
s41 <- propagate_s(models$vdp_s, init=init[1,], par=parvdps, 
                   times, Astro=Astro, seed=95) 

# we selected here the 'fourth' pullback attractor
# chosen after some trial and error to be representative
# of the phenomenon we want to illustrate

p40 <- pullback_d(models$vdp_d, times=times, par=parvdp40, Astro=Astro)$S[[4]]

# ... and save ! 
save(file='../RData/pullback_11.RData', p41, s41, p40,times)


