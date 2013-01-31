require(iceages)

# this routine calculates the 'cardinality diagram' for 
# any of the foreign models. They are all configured
# the same way. We only need to browse the 'gamma / omega '
# parameter space and use the functions embedded in 
# the 'icaeges' package, so this should be pretty straightforward
# note though that with the full resolution the present
# code may easily take one week or so on a multi-core machine


# the list where all the output will be stored 

KList <- list ()

# we use tback = -2 Ma, as a compromise. Saltzman models would
# normally require far deeper tback, but anyway this is irrelevant
# at the time scale of the Pleistocene, and the graphics obtained
# this way offer a good enough visual acconut of the structural
# stability of the systems. 

tback <- -200.

for (modelname in c("pp12_d","cr12_d","i11_d","t06_d","pp04_d","s90_d","s91_d"))
{
  model <- models[[modelname]]
  Astro <- read_astro(34,34)

  gamma <- seq(0.02,1.5,0.002)
  omega <- seq(0.5,1.5,0.002)

  par <- as.list(model$spar)
  par$gamma = gamma
  par$omega = omega

  par <- expand.grid(par)

  # deltat is adjusted to omega, we generally
  # expect the equations to scale in tame
  # with omega. 
  # A time step of 0.03 * omega is somewhat ad-hoc. 
  # In the near future we may want to adjust it from one
  # model to the next. Should'nt be that difficult. 

  deltat=0.03*par[,'omega']

  t_back <- as.numeric(tback)
  t0 <- as.numeric(0. )
  N <- nrow(par)
  count  <- rep(0, N)

  count <- compute_cluster(model, par, tback=t_back, t0=t0, Astro=Astro, ncores=10, deltat=deltat)

  # reshape as a matrix

  count <- list(x=omega, y=gamma, z=t(matrix(count, length(gamma), length(omega))))
  attr(count,"name") <- model$name

  KList[[modelname]] <- count

  # save repeatedly, never know the program would crash and everything would be lost
  save(file='KList_Others.RData', KList)

}

