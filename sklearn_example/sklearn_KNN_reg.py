import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_regression
from sklearn.neighbors import KNeighborsRegressor

x, y = make_regression(n_features=1, n_informative=1, noise=50, random_state=8)
plt.scatter(x, y, c='orange', edgecolors='k')
# plt.show()

reg = KNeighborsRegressor(n_neighbors=5)
reg.fit(x, y)

z = np.linspace(-3, 3, 200).reshape(-1, 1)
plt.plot(z, reg.predict(z), c='k', linewidth=3)
plt.title('Classifier:KNN')
print('模型正确率：', reg.score(x, y))
plt.show()
