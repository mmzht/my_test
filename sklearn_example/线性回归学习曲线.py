import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.model_selection import learning_curve, KFold


def plot_learning_curve(est, x, y):
    training_set_size, train_scores, test_scores = learning_curve(est, x, y, train_sizes=np.linspace(0.1, 1, 20),
                                                                  cv=KFold(20, shuffle=True, random_state=1))
    estimator_name = est.__class__.__name__
    line = plt.plot(training_set_size, train_scores.mean(axis=1), '--', label="training" + estimator_name)
    plt.plot(training_set_size, test_scores.mean(axis=1), '-', label="test" + estimator_name, c=line[0].get_color())
    plt.xlabel('training set size')
    plt.ylabel('score')
    plt.ylim(0, 1, 1)


x, y = load_diabetes().data, load_diabetes().target
plot_learning_curve(Ridge(alpha=1), x, y)
plot_learning_curve(LinearRegression(), x, y)
plt.legend(loc=(0, 1.05), ncol=2, fontsize=11)
plt.show()
