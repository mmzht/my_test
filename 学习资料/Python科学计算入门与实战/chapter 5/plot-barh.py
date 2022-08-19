import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['axes.unicode_minus'] = False

category_names = ['强烈反对', '反对',
                  '中立','同意', '强烈同意']
results = {
    '问题 1': [10, 15, 17, 32, 26],
    '问题 2': [26, 22, 29, 10, 13],
    '问题 3': [35, 37, 7, 2, 19],
    '问题 4': [32, 11, 9, 15, 33],
    '问题 5': [21, 29, 5, 5, 40],
    '问题 6': [8, 19, 5, 30, 38]
    }

labels = list(results.keys())
data = np.array(list(results.values()))
data_cum = data.cumsum(axis=1)
category_colors = ["red","yellow","green","cyan","pink"]
fig, ax = plt.subplots(figsize=(10, 5))
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=1).max())
for i, (colname, color) in enumerate(zip(category_names, category_colors)):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    ax.barh(labels, widths, left=starts, height=0.5,
            label=colname, color=color)
    xcenters = starts + widths / 2
    for y, (x, c) in enumerate(zip(xcenters, widths)):
        ax.text(x, y, str(int(c)), ha='center', va='center')
ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1.02),
          loc='lower left', fontsize='small')
plt.show()
