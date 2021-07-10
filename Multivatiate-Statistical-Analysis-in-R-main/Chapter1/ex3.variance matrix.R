data(mtcars)

# 각 변수에 대한 공분산행렬 계산
cov(mtcars[,c('disp','hp','wt','qsec')])

# 각 변수에 대한 상관행렬 계산
cor(mtcars[,c('disp','hp','wt','qsec')])

# am = 0 일 때, 각 변수에 대한 공분산행렬 계산
cov(subset(mtcars,am==0)[,c('disp','hp','wt','qsec')])

# am = 1 일 때, 각 변수에 대한 상관행렬 계산
cor(subset(mtcars,am==1)[,c('disp','hp','wt','qsec')])