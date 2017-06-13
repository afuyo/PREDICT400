K <- 11 # Eftersom att vi spelar Keno 
p <- rep(0, K + 1) #En vektor som kommer tilldelas sannolikheterna för 0, 1, ..., K antal rätt. Detta betyder  att p[1] ger sannolikheten för 0 rätt så p[K+1] ger sannolikheten för K (i detta fall 11) rätt.
for (k in 0:K) {
  p[k+1] <- choose(20,k)*choose(50,11-k)/choose(70,11) # p[k+1] är alltså sannolikheten att få k rätt
}
v<-c(1:70)
a<-sample(v,20)
for(i in 0:1000) {
  a<-append(a,sample(v,20))
}

hist(a,breaks=v,main="Keno 11",xlab='After 1000 rounds')
