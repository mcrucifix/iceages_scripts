# ncores to be set as a function of the computer, and
# whether it can serve solely to your own purpose or whether
# you need to share it. 

NCORES = 11 

## 

require(iceages)

# this routine calculates the 'cardinality diagram' for 
# the vanderpol model. 
# We only need to browse the 'gamma / omega '
# parameter space and use the functions embedded in 
# the 'icaeges' package, so this should be pretty straightforward
# note though that with the full resolution the present
# code may easily take one week or so on a multi-core machine

model <- models$vdp_d

gamma <- seq(0.02,1.5,0.002)
omega <- seq(0.5,5.0,0.005)


par <- as.list(model$spar)

# we face a small design issue. Given that omega comes after gamma,
# omega will be the slowly varying parameter in the expand.list below.
# Given that deltat is proportional to omega, the multi-core distribution
# will be unequal.
# so what we do is a bit cheating. We will make "alpha" to vary
# is if it were OMEGA, and then swap the columns


tmpalpha = par$ALPHA

par$GAMMAPRE = gamma
par$ALPHA = omega

par <- expand.grid(par)

# Unlike the 'foreign' models, the vanderpol model
# features two parameters controlling the amplitude
# of the forcing : GAMMAPRE and GAMMAOBL.
# however, for this application, we want GAMMAPRE = GAMMAOBL
# so we construct the grid assuming only GAMMAPRE varies,
# and then set GAMMAOBL = GAMMAPRE. 

par[,'GAMMAOBL'] = par[,'GAMMAPRE']

# ok, so now swap:

par[,'omega'] = par[,'ALPHA']
par[,'ALPHA'] = tmpalpha 

# and trash garbage
rm('tmpalpha')

## deltat is adjusted to omega, because
## the numerical equations  scale in tame

deltat=0.005*par[,'omega']

# we are here pretty ambitious, we use
# tback = - 10 Ma ( = -1000 * 10 ka )
# but this is what will give us the crispiest
# looking graphics ! 

t_back <- as.numeric(-1000. )

t0 <- as.numeric(0. )

N <- nrow(par)
count  <- rep(0, N)

# ok. Everything is set up. Now we can prepare the graphs one by one. 
# KList is where we will store all the output

KList <- list()

# 1. Use only precession (periodic forcing)

Astro <- read_astro(1,0)
count <- compute_cluster(model, par, tback=t_back, t0=t0, 
                          Astro=Astro, ncores=NCORES, deltat=deltat)
count <- list(x=omega, y=gamma, z=matrix(count), length(omega), length(gamma))
attr(count,"name") <- "Periodic forcing ($P_1$)"
KList[["periodic"]] <- count 


# 2. First component of precession and obliquity

Astro <- read_astro(1,1)
count <- compute_cluster(model, par, tback=t_back, t0=t0, 
                          Astro=Astro, ncores=NCORES, deltat=deltat)
count <- list(x=omega, y=gamma, z=matrix(count, length(omega), length(gamma)))
attr(count,"name") <- "Quasi-periodic forcing ($P_1$ and $E_1$)"
KList[["2periods"]] <- count 

# 3. Components 2 and 3 of precession

# needs a bit of thinkering here ... 
Astro <- read_astro(3,0)
Astro$nap <- 2
for (j in c('amppre','omepre','angpre'))  Astro[[j]] <- Astro[[j]][c(2,3)]

count <- compute_cluster(model, par, tback=t_back, t0=t0, 
                          Astro=Astro, ncores=NCORES, deltat=deltat)
count <- list(x=omega, y=gamma, z=matrix(count, length(omega), length(gamma)))
attr(count,"name") <- "2-period forcing ($P_2$ and $P_3$)"
KList[["precess"]] <- count 

# 4. And finally full forcing:
Astro <- read_astro(34,34)
count <- compute_cluster(model, par, tback=t_back, t0=t0, 
                          Astro=Astro, ncores=NCORES, deltat=deltat)
count <- list(x=omega, y=gamma, z=matrix(count, length(omega), length(gamma)))
attr(count,"name") <- "Full astronomical forcing"
KList[["astro"]] <- count 

save(file='Klist_vdp.RData',KList)



