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
pdf('Pdf/figure1.pdf', height=6, width=5, pointsize=11)
Astro <- read_astro(31,31)
times=seq(-80,0,0.2)

# Saltzman 90 with standard parameters
# uses model such as directly coded in Insol package
# with some carefully chosen initial conditions 

sm90_standard <- propagate_d(models$s90_d, init=c(-0.1, 0.2, .5), 
                             par=c(1., 1., w=0.5), 
                             times=times, Astro=Astro);

# no we repeat, but tweaking w a little bit

sm90_perturbed <- propagate_d(models$s90_d, init=c(-0.1, 0.2, .5), 
                              par=c(1., 1., w=0.6), times=times, Astro=Astro);

# do the same with the Tziperman et al. 2006 model...

t06_standard <- propagate_d(models$t06_d, init=c(42.0 ,0.), 
              par=c(1.0, 1., p0=0.26, s=0.23, sm=0.03), 
              times=times, Astro=Astro);

# tweaking p0 only slightly

t06_perturbed <- propagate_d(models$t06_d, init=c(42., 0.), 
        par=c(1.0, 1., p0=0.2620, s=0.23, sm=0.03), 
        times=times, Astro=Astro);

par(mfrow=c(3,1))
par(mar=c(4,4,2,1))
par(cex=1.1)

# recontsruct standard insolation, 
# these gp and go allow to reconstruct
# normalised insol 65N insolation

gp = 0.7639; go = 0.4756
f   = gp * sm90_standard[,4] + go * sm90_standard[,5]

# and plot

plot(times*10,f, type='l', col='black', xlab='time [ka]', main='Forcing (mid-June insolation at 65N)', frame=FALSE, axes=FALSE, ylab='A.U.')
axis(1, at = -seq(0,8)*100)
axis(2)

plot(times*10,sm90_standard[,1], type='l', col='blue', 
    xlab='time [ka]', ylab='Ice volume (A. U.)', 
    main='Saltzman and Maasch 1990', frame=FALSE, axes=FALSE)

lines(times*10,sm90_perturbed[,1], type='l', col='red')
axis(1, at = -seq(0,8)*100)
axis(2, at=c(-1,0,1))


plot(times*10,t06_standard[,1], type='l', col='blue',
    xlab='time [ka]', ylab='Ice volume (1E15 m3)',
    main='Tziperman et al., 2006', frame=FALSE, axes=FALSE)

lines(times*10,t06_perturbed[,1], type='l', col='red')
axis(1, at = -seq(0,8)*100)
axis(2)


dev.off()
