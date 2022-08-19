import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.api as sm  # 评估线性回归模型

plt.rcParams['font.sans-serif'] = 'simHei'  # 解决中文字体乱码
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

x = np.arange(50).reshape(-1, 1)
y = 0.1 * np.arange(50) ** 2 + np.random.randint(1, 60, size=50)
poly_reg = PolynomialFeatures(degree=2)  # 一元二次拟合
x_ = poly_reg.fit_transform(x)
regr = LinearRegression().fit(x_, y)  # 模型搭建

print('拟合的公式：y=%.3fx+%.3fx**2+%.3f' % (regr.coef_[1], regr.coef_[2], regr.intercept_))  # 模型系数
prediction = regr.predict([[1, 5.4, 5.4 * 5.4], [1, 9.7, 9.7 * 9.7]])  # 应用模型预测结果，[1,x,x*x]三个数
print('5.4，9.7预测结果：', prediction)

plt.scatter(x, y, s=60, c='b')
plt.plot(x, regr.predict(x_), c='r')  # 你和的直线
plt.title('Linear Regression线性回归(一元二次)')
plt.show()

# 模型评估
x2 = sm.add_constant(x_)  # 增加y=k*x+b的常数项b
est = sm.OLS(y, x2).fit()  # 线性回归方程搭建
print(est.summary())  # 二次项的显著性较差
