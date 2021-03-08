import numpy as np
import pandas as pd
import math

np.random.seed(1)


# make gaussian distribution
def getSampling(mean, cov, size):
    mul = np.random.multivariate_normal(mean, cov, size)
    return mul


def getSamplingExMean(mul):
    c = np.mean(mul, axis=0)
    mul_t = mul - np.mean(mul, axis=0)
    return mul_t


mean = (10, -10)
cov = np.array([[34, 12], [12, 41]])
mul_t = getSampling(mean, cov, 100)
mean1 = (15, 25)
cov1 = np.array([[10, -2.5*math.sqrt(3)], [-2.5*math.sqrt(3), 5]])
mul_t1 = getSampling(mean1, cov1, 100)
# vstack是合并两个矩阵的函数
mul_final = np.vstack((mul_t, mul_t1))
mul_final_exMean = getSamplingExMean(mul_final)
np.savetxt('new4.csv', mul_final, delimiter=',')
print(mul_final_exMean)

# PCA
P = np.dot(mul_final_exMean.T, mul_final_exMean)
Q = P / mul_final_exMean.size
# SVD
U, sigma, VT = np.linalg.svd(Q)
print(U)

# calculate principle parameter
X = np.dot(mul_final_exMean, U)
np.savetxt('one4.csv', X, delimiter=',')
print(X)
