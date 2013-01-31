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

# computes rayleigh number on eccentricity beating
# this is a 'pseudo-eccentricity', arising
# from the combination of tones 2 and 3 of eccentricity
# see text for details

require(iceages)
data(models)

model <- models$vdp_d

NCORES = 5.

# use model standard parameters
par <- as.list(model$spar) 

# as in 'card_vdp' we construct a parameter list
# spanning  forcing amplitude and timescale

gamma <- seq(0.02,1.5,0.2)
omega <- seq(0.5,5.0,0.5)

par$GAMMAPRE = gamma
par$omega = omega

par <- expand.grid(par)

par[,'GAMMAOBL'] = par[,'GAMMAPRE']

## deltat is adjusted to omega, because
## the numerical equations  scale in tame

deltat=0.02*par[,'omega']

# initial conditions will be estimated from 
# a generous pullback of -3 Ma ! 

t_0 = as.numeric(-300000.)
t_1 = as.numeric(-0.)

# same tweak as in card_vdp : we use
# components 2 and 3 of precession,
# for reasons made clear in the article

Astro <- read_astro(3,0)
Astro$nap <- 2
for (j in c('amppre','omepre','angpre'))  Astro[[j]] <- Astro[[j]][c(2,3)]

# so , now that only the two first components are
# left, we compute the eccentricity beating period:
DT=2*pi/(Astro$omepre[2]-Astro$omepre[1]) 

# use some dummy initial condition: not very important
init = c(0.1,0.1)

# and so we only need to use the rayleigh function
# supplied in the insol package

K <- rayleigh(model, as.matrix(par), init, t_0, t_1, DT, 
              n = as.integer(500), ncores = NCORES, 
              Astro=Astro, deltat=deltat )

# packs up and save
KK <- list(x=omega, y=gamma, z=t(matrix(count, length(gamma), length(omega))))
KK <- list(x=omega, y=gamma, z=K)
save(file='RData/Ray.RData', KK )


