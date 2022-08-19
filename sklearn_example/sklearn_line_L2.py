from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

x, y = load_diabetes().data, load_diabetes().target
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=8)
ridge = Ridge(alpha=0.1).fit(x_train, y_train)

print('训练数据集得分：', ridge.score(x_train, y_train))
print('测试数据集得分：', ridge.score(x_test, y_test))
