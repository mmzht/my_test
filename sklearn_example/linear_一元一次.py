import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
import statsmodels.api as sm  # 评估线性回归模型

plt.rcParams['font.sans-serif'] = 'simHei'  # 解决中文字体乱码
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

x, y = make_regression(n_samples=50, n_features=1, n_informative=1, noise=20, random_state=1)
'''
n_samples：样本数
n_features：特征数(自变量个数)
n_informative：参与建模特征数
n_targets：因变量个数
noise：噪音
bias：偏差(截距)
coef：是否输出coef标识
random_state：随机状态若为固定值则每次产生的数据都一样
'''
regr = LinearRegression().fit(x, y)  # 模型搭建
print('拟合的公式：y=%.3fx+%.3f' % (regr.coef_[0], regr.intercept_))  # 模型系数
# 预测
prediction = regr.predict([[1.4], [1.7]])  # 应用模型预测结果，只有一个数时需要两个中括号
print('1.4，1.7预测结果：', prediction)
# 绘图
plt.scatter(x, y, s=60, c='b')
plt.plot(x, regr.predict(x), c='r')  # 你和的直线
plt.title('Linear Regression线性回归')
plt.show()
# 模型评估
x2 = sm.add_constant(x)  # 增加y=k*x+b的常数项b
est = sm.OLS(y, x2).fit()  # 线性回归方程搭建
print(est.summary())

from sklearn.metrics import r2_score

print('评分方式1', r2_score(y, regr.predict(x)))
print('评分方式2', regr.score(x,y))
'''
                             OLS Regression Results：评估结果
==============================================================================
Dep. Variable:                      y   R-squared:                       0.963（R平方值）
Model:                            OLS   Adj. R-squared:                  0.962(考虑变量数量的R方)
Method:                 Least Squares   F-statistic:                     1258.
Date:                Fri, 09 Jul 2021   Prob (F-statistic):           4.31e-36
Time:                        20:55:07   Log-Likelihood:                -210.48
No. Observations:                  50   AIC:                             425.0
Df Residuals:                      48   BIC:                             428.8
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err        t   P>|t|（显著性）   [0.025      0.975]显著性小于0.05认为是显著特征，越小越显著
------------------------------------------------------------------------------
const      4.3689（常数项）  2.352      1.857      0.069      -0.361       9.098
x1        86.0140（一次项）  2.425     35.468      0.000      81.138      90.890
==============================================================================
Omnibus:                        0.567   Durbin-Watson:                   1.975
Prob(Omnibus):                  0.753   Jarque-Bera (JB):                0.105
Skew:                          -0.041   Prob(JB):                        0.949
Kurtosis:                       3.208   Cond. No.                         1.04
==============================================================================
'''
