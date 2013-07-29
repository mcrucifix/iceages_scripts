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

Astro <- read_astro(34,34)
times=seq(-40,10,0.1)

# determinstic parameter set
#parvdp  = c(alpha=30.0, beta=0.7,  gammapre=0.6, gammaobl=0.6,
#            omega=3.60, asym=0)


parvdp  = c(alpha=30.0, beta=0.7,  gammapre=1.0, gammaobl=1.0,
            omega=3.60, asym=0)

# stochastic parameter set
#parvdps = c(alpha=30.0, beta=0.7,  gammapre=0.6, gammaobl=0.6, 
#            omega=3.60, sigma=0.5)


parvdps = c(alpha=30.0, beta=0.7,  gammapre=1.0, gammaobl=1.0, 
            omega=3.60, sigma=0.5)
# initial conditions positioned on the pullback attractor at time 0
# we do this rather than using the convenient 'pullaback_d' because
# we want to be able to restart from the same IC with the stochastic model

init <- basin(models$vdp_d, par=parvdp, -2500., times[1],  Astro=Astro)$clusters

p36 <- list()
for (i in seq(nrow(init)))
 {
  p36[[i]] <- propagate_d(models$vdp_d, times, init=init[i,], par=parvdp, Astro=Astro)
 }

# tweaks the paramer 
parvdp38 = parvdp; parvdp38['omega'] = 3.8 
parvdp34 = parvdp; parvdp34['omega'] = 3.39

s36 <- list();

# generates the 'stochastic' and 'deterministic' tweaked attractors
# 30 samples of stochastic, do provide a distribution
for (i in seq(30))
{
  s36[[i]] <- propagate_s(models$vdp_s, init=init[1,], par=parvdps, 
                   times, Astro=Astro, seed=25+i) 
}

# we selected here the 'fourth' pullback attractor
# chosen after some trial and error to be representative
# of the phenomenon we want to illustrate

p38 <- pullback_d(models$vdp_d, times=times, par=parvdp38, Astro=Astro)$S[[1]]
#p37 <- pullback_d(models$vdp_d, times=times, par=parvdp37, Astro=Astro)$S[[1]]
#p35 <- pullback_d(models$vdp_d, times=times, par=parvdp35, Astro=Astro)$S[[1]]
p34 <- pullback_d(models$vdp_d, times=times, par=parvdp34, Astro=Astro)$S[[1]]

# ... and save ! 
save(file='../RData/pullback_34.RData', p36, s36, p38,times)


