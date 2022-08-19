import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

x, y = make_regression(n_samples=100, n_features=2, n_informative=2, noise=10, random_state=8)
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=8)

lr = LinearRegression().fit(x_train, y_train)
print('拟合的公式：y=%.3fx1+%.3fx2+%.3f' % (lr.coef_[0], lr.coef_[1], lr.intercept_))

print('训练数据集得分：', lr.score(x_train, y_train))
print('测试数据集得分：', lr.score(x_test, y_test))

# 绘制散点图
plt.rcParams['font.sans-serif'] = 'simHei'  # 解决中文字体乱码
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
plt.figure(figsize=(8, 6))  # 设置画布大小
ax = plt.axes(projection='3d')  # 设置三维轴
ax.scatter3D(x[:, 0], x[:, 1], y)  # 三个数组对应三个维度
z = 7.485 * x[:, 0] + 83.718 * x[:, 1] + 0.567  # 拟合公式
ax.scatter3D(x[:, 0], x[:, 1], z)  # 三个数组对应三个维度
plt.title('Linear Regression两个变量的线性回归')
plt.show()
