

#install.packages('OpenImageR')
library(OpenImageR)
x<-readImage('../data/mt-15-front-view.jpeg')
dim(x)
x= resizeImage(x, dim(x)[1],dim(x)[2], method = 'bilinear')
# plot(0, type='n', axes =F, xlab="",ylab="")
imageShow(x)
r<-rgb_2gray(x)
# plot(0, type='n', axes =F, xlab="",ylab="")
imageShow(r)

## SVD 적용
r.svd<-svd(r)
d <-diag(r.svd$d)
dim(d)

u<-r.svd$u
v<-r.svd$v
plot(1:length(r.svd$d),r.svd$d)

## SVD 근사
# 1개의 특이값을 이용한 근사 
u1<-as.matrix(u[-1,1])
v1<-as.matrix(v[-1,1])
d1<-as.matrix(d[1,1])
l1<-u1%*%d1%*%t(v1)
# plot(0, type='n', axes = F, xlab="",ylab="")
imageShow(l1)

# 5개의 특이값을 이용한 근사
depth <-5 # k=20,30,50,100,150에 대해서도 적용
us <- as.matrix(u[,1:depth])
vs<-as.matrix(v[,1:depth])
ds<-as.matrix(d[1:depth,1:depth])
ls<-us%*%ds%*%t(vs)
#plot(0, type='n',axes = F, xlab="",ylab="")
imageShow(ls)

## 컬러 이미지로 근사

depth <-30 # k=30으로 근사
for(i in 1:3){
  x.svd <- svd(x[,,i])
  d<-diag(x.svd$d)
  u<-x.svd$u
  v<-x.svd$v
  us<-as.matrix(u[,1:depth])
  vs<-as.matrix(v[,1:depth])
  ds<-as.matrix(d[1:depth,1:depth])
  assign(paste("ls",i,sep=""),us %*% ds %*% t(vs))
}
ls<-array(c(ls1,ls2,ls3),c(nrow(ls1),ncol(ls1),3))
plot(0,type='n',axes=F,xlab="",ylab="")
imageShow(ls)