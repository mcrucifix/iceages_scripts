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
require(pleistocene)
data(LR04)
data(models)

Astro <- read_astro(34,34)
times=seq(-70,0,0.2)

parvdp = c(30.0, 0.75,  0.6, 0.6, 3.62, 0)
vdp_standard <- propagate_d(models$vdp_d, init=c(-0.7, -0.4), par=parvdp, times=times, Astro=Astro);
shift=4.2
decishift=shift-floor(shift)

pdf('Pdf/vdpfit.pdf', height=5, width=6)

par(mfrow=c(1,1))
par(mar=c(1,5,3,5))
par(oma=c(4,0,0,0))
plot(times*10, vdp_standard[,1], type='l', col='black', xlab='time [ka]', 
              ylab = 'x', 
              main='van der Pol oscillator forced by astronomical forcing', 
              frame=FALSE)
mtext(side = 4, line=3, text= 'LR04 delta-18 O', col='blue')
points(-LR04$Age.ka,   LR04$Forambenthd18O.permilPDB - shift, col='blue')
axis(1, at=-seq(1,8)*100)
axis(4, at=seq(-1,1,0.5)-decishift, labels=seq(-1,1,0.5)+shift-decishift, col='blue', col.ticks='blue')

#plot(times*10, vdp_standard[,2], type='l', col='black', 
#              xlab='time [ka]', ylab = 'y', frame=FALSE)
#axis(1, at=-seq(1,8)*100)
#
mtext(side=1, outer=TRUE, line=3, text='Time [ka] ')

dev.off()
