K <- 11 # Eftersom att vi spelar Keno 
p <- rep(0, K + 1) #En vektor som kommer tilldelas sannolikheterna f�r 0, 1, ..., K antal r�tt. Detta betyder  att p[1] ger sannolikheten f�r 0 r�tt s� p[K+1] ger sannolikheten f�r K (i detta fall 11) r�tt.
for (k in 0:K) {
  p[k+1] <- choose(20,k)*choose(50,11-k)/choose(70,11) # p[k+1] �r allts� sannolikheten att f� k r�tt
}
v<-c(1:70)
a<-sample(v,20)
for(i in 0:1000) {
  a<-append(a,sample(v,20))
}

hist(a,breaks=v,main="Keno 11",xlab='After 1000 rounds')
