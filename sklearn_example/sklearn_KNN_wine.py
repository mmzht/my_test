from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

wine_dataset = load_wine()
x_train, x_test, y_train, y_test = train_test_split(wine_dataset['data'], wine_dataset['target'], random_state=0)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train, y_train)
print('测试集得分：', knn.score(x_test, y_test))
x_new = np.array([[13.2, 2.77, 2.51, 18.5, 96.6, 1.04, 2.55, 0.57, 1.47, 6.2, 1.05, 3.33, 820]])
prediction = knn.predict(x_new)
print('预测x_new的分类：', wine_dataset['target_names'][prediction])
