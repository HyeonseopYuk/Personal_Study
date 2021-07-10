round(dist(trees),2) # 개체들 간의 유클리드 거리

dist(scale(trees, center=FALSE)) # 척도화된 거리

dist(scale(trees,center=TRUE)) # 표준화(중심화+척도화)된 거리
