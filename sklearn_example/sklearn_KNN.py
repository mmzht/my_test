from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np

data = make_blobs(n_samples=500, centers=4, random_state=6)
x, y = data  # 实例数据集
# plt.scatter(x[:,0],x[:,1],c=y,cmap=plt.cm.spring,edgecolors='k')
# plt.show()

clf = KNeighborsClassifier()
clf.fit(x, y)
# 画图数据
x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))
z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = z.reshape(xx.shape)
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Pastel1, shading='auto')
plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.spring, edgecolors='k')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('Classifier:KNN')
plt.scatter(6.75, 4.82, marker='*', c='r', s=200)
print('新数据点6.75, 4.82的分类：', clf.predict([[6.75, 4.82]]))
print('模型正确率：', clf.score(x, y))
plt.show()
