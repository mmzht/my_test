from sklearn.linear_model import LogisticRegression
import pandas as pd

x = [[1, 0], [5, 1], [6, 4], [4, 2], [3, 2]]
y = [0, 1, 1, 0, 0]
model = LogisticRegression().fit(x, y)

model.predict([[2, 2]])  # 使用模型预测

y_pred_proba = model.predict_proba(x)  # 分类的概率数值
result = pd.DataFrame(y_pred_proba, columns=['分类为0的概率', '分类为1的概率'])
print(result)
print('模型系数和截距：', model.coef_, model.intercept_)


