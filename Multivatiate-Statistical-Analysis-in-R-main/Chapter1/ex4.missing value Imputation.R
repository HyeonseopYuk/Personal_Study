# 분석자료
air <- airquality[,1:4]
air[11:15,3] <- NA # 결측값 추가
air[51:55,4] <- NA # 결측값 추가
summary(air) # 결측값 확인


# 기초분석 : 변수별 결측값의 수와 결측값의 형태를 파악
#install.packages('mice')
library(mice)
md.pattern(air)

# * 패키지 {VIM}은 결측값의 패턴을 시각화하는 데 유용하다. 여기서는 aggr()과 marginplot() 함수를 통해 표현.

# aggr()함수 : 결측(/대치)값에 대한 집계 제공
#install.packages('VIM')
library(VIM)
aggr(air, col=c('skyblue','red'),numbers=TRUE, sortVars=TRUE,
     labels = names(air), cex.axis=.7, gap=3, ylab=c("Percentage of missing","Missing Pattern"))

# marginplot() 함수 : 변수 쌍에 대한 산점도와 함께 결측(/대치)값에 대한 정보를 마진에 그림으로 제공
marginplot(air[c(1,2)])


####
# 다중 대치의 수를 5개로 지정하고, method ='pmm' 적용 : 각 관측값에 대해 해당 변수에 가장 가까운 예측 평균을 가진 관측값으로 대치

air.m<-mice(air,m=5, maxit=50, meth='pmm',seed=2000)

# 결측값이 대치된 완비 자료는 complete() 함수를 이용하여 출력할 수 있다.

ls(air.m)
summary(air.m)

#결측값 대치 후의 완비 자료 출력(5개 중 첫 번째 사용)
air.com<-complete(air.m,1)

xyplot(air.m, Ozone~Wind+Temp+Solar.R, pch=18, cex=1)
densityplot(air.m)
stripplot(air.m, pch=20, cex = 1.2)

# 또한, 다중 대치에 의한 여러 개의 완비 데이터 셋별로 특정 모형을 적합한 뒤, 이를 결합하는 방법을 제시하면 다음과 같다.
fit1 <- with(air.m, lm(Temp~ Ozone+Solar.R+Wind))
summary(pool(fit1))
air.m2<-mice(air,m=50, seed=500)
fit2<-with(air.m2,lm(Temp~Ozone+Solar.R+Wind))
summary(pool(fit2))
