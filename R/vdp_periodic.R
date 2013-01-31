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


## dummy file. Was used to generate vdp 
## responses to a periodi forcing,
## as a background to draw the Inskape figure
## illustrating the difference between pullback attractor
## and stroboscopic section

## parameters were chose as to have a 2-1 resonance


require(iceages)
pdf('figure1.pdf', height=8, width=8, pointsize=14)
Astro <- read_astro(1,0)
omega = Astro$omepre[1]
P = 2*pi / omega
times=c(-100,seq(-0.2, 2.2,0.02)*P)
phi = times*omega


vdppar <- c(3, 0.3, 0.7, 0., 1.090135, 0.)
vdp<- propagate_d(models$vdp_d, init=c(0.1,0.1), par=vdppar,  times=times, Astro=Astro)

vdp = vdp[,1:3]
vdp [,3] = vdp [,3] * 0.
vdp = vdp[-1,]

for (i in seq(nrow(vdp)))
 {
 # phi = phi*0. 
  sp = sin(phi[i]) ; cp = cos(phi[i])
  m = matrix( c(1, 0, 0, 0, cp, sp, 0, -sp, cp), 3,3,byrow=TRUE)
   vdp[i,] = m %*% ( ( vdp[i,]*0.03 + c(1.0, 1.0, 0) ) )
 #  vdp[i,3] = sp
 }


write.table(file='loop.dat', vdp, row.names=FALSE, col.names=FALSE)

## now  the pullback attractor and three sample trajectories

times = seq(0,40,0.2)
pull<- pullback_d(models$vdp_d, init=c(0.1,0.1), par=vdppar,  times=times, Astro=Astro, back=-500)

for (i in seq(along=pull$S))
{
  write.table(cbind(times,pull$S[[i]]), file=sprintf('pull_%i.dat',i), row.names=FALSE, col.names=FALSE)
}

init = expand.grid(seq(-1,1,0.2),seq(-1,1,0.2))
for (i in seq(dim(init)[1]))
{
  fwd <- propagate_d(models$vdp_d, init = as.numeric(init[i,]), par=vdppar, times=times, Astro=Astro)
  write.table(cbind(times,fwd), file=sprintf('fwd_%3i.dat',i), row.names=FALSE, col.names=FALSE)
}

