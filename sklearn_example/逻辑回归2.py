import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import numpy as np

cancer_dataset = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(cancer_dataset['data'], cancer_dataset['target'], test_size=0.2,
                                                    random_state=1)
# print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

model = LogisticRegression(solver='liblinear').fit(x_train, y_train)

print('训练集得分：', model.score(x_train, y_train))
print('测试集得分：', model.score(x_test, y_test))
from sklearn.metrics import accuracy_score

score = accuracy_score(model.predict(x_test), y_test)
print('测试集得分：(另一种实现方式)', score)

y_pred_proba = model.predict_proba(x_test)  # 分类的概率数值
result = pd.DataFrame(y_pred_proba, columns=['分类为0的概率', '分类为1的概率'])
result['预测值'] = model.predict(x_test)
result['实际值'] = y_test
print(result)

x_new = np.array([21.56, 22.39, 142, 1479, 0.111, 0.1159, 0.2439, 0.1389, 0.1726, 0.05623, 1.176, 1.256, 7.673, 158.7,
                  0.0103, 0.02891, 0.05198, 0.02454, 0.01114, 0.004239, 25.45, 26.4, 166.1, 2027, 0.141, 0.2113,
                  0.4107, 0.2216, 0.206, 0.07115])  # 实际分类为0
prediction = model.predict([x_new])  # 使用模型预测
print('预测x_new的分类：', prediction)

from sklearn.metrics import classification_report

print(classification_report(y_test, model.predict(x_test)))  # 分类报告
from sklearn.metrics import roc_curve

# ROC曲线
fpr, tpr, thres = roc_curve(y_test, y_pred_proba[:, 1])
roc = pd.DataFrame()
roc['假报率'] = fpr
roc['命中率'] = tpr
roc['阈值'] = thres
print(roc)
import matplotlib.pyplot as plt

plt.plot(fpr, tpr, c='b')
plt.title('ROC plot')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.show()

from sklearn.metrics import roc_auc_score

score = roc_auc_score(y_test, y_pred_proba[:, 1])
print('AUC值：', score)
# KS曲线
plt.plot(thres[1:], tpr[1:], c='b')
plt.plot(thres[1:], fpr[1:], c='r')
plt.plot(thres[1:], tpr[1:] - fpr[1:], c='g')
plt.title('KS plot')
plt.legend(['TPR', 'FPR', 'TPR-FPR'])
plt.gca().invert_xaxis()
plt.show()
print('KS值：', max(tpr - fpr))
