require(iceages)

Astro = read_astro(34,34)
times = seq(-80,0,0.1)
data(models)

PULL <- list()

 for (modelname in c('pp04','pp12','t06','i11','s90','s91'))
 {
   fullmodelname = paste(modelname,"_d",sep="")
   cat(sprintf("handling model %s \n", fullmodelname))
   model <- models[[fullmodelname]]
   print(model)

   PULL[[modelname]] <- pullback_d (model, par=model$spar, t_back = -2000, 
                                    times=times, Astro, deltat=0.01)
   attr(PULL[[modelname]], "name") <-  toupper(modelname)
 }

save(file='RData/pullback_others.RData', PULL)
