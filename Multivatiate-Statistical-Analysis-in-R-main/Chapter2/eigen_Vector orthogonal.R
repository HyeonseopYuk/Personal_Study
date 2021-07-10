### 행렬의 교차곱(cross-product): X.transpose() * Y

crossprod(ev$vectors) # 인자가 한 개인 경우는 X.transpose() X 와 동일

# zapsmall() 함수는 영(zero)에 가까운 값을 영으로 처리함(zapped).
zapsmall(crossprod(ev$vectors))
