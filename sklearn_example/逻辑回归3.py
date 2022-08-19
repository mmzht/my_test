import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

iris_dataset = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
# print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

model = LogisticRegression(solver='liblinear').fit(x_train, y_train)

print('训练集得分：', model.score(x_train, y_train))
print('测试集得分：', model.score(x_test, y_test))
y_pred_proba = model.predict_proba(x_test)  # 分类的概率数值
result = pd.DataFrame(y_pred_proba, columns=['分类为0的概率', '分类为1的概率', '分类为2的概率'])
result['预测值'] = model.predict(x_test)
result['实际值'] = y_test
# print(result)

x_new = np.array([5.4, 3.7, 1.5, 0.2])
prediction = model.predict([x_new])  # 使用模型预测
print('预测x_new的分类：', prediction)

from sklearn.metrics import classification_report
print(classification_report(y_test, model.predict(x_test)))  # 分类报告
