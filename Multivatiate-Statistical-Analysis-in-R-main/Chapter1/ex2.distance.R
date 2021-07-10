x<-matrix(rnorm(100*3), ncol=3)

# 공분산 계산하기 위함
Sx<-cov(x)

# 자료의 평균과 공분산행렬을 옵션으로 지정함
D2<- mahalanobis(x,colMeans(x),Sx)
round(D2,2)

