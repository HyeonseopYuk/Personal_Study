A<-matrix(c(13,-4,2,-4,11,-2,2,-2,8),3,3,byrow=TRUE)
A

ev <- eigen(A)
ev$values # 고유값

ev$vectors # 고유벡터

