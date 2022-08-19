import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

filename = r'D:\python\data\excelfile.xlsx'  # 带路径的文件名
save_file = r'D:\python\data\savefile.xlsx'  # 结果保存文件

# use_cols_list = [1, 3, 5, 6, 8]或usecols=range(7)  #usecols=use_cols_list, header=None, index_col=None，nrows=8
df = pd.read_excel(filename, sheet_name=0, index_col=None)
# print(df.head(9))

plt.rcParams['font.sans-serif'] = 'simHei'  # 解决中文字体乱码
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# fig = plt.figure(figsize=(8, 6))  # 对象式添加，语句多，含义明确
# ax1 = fig.add_subplot(111)
# ax2 = fig.add_subplot(222)

'''
plt.style.use('tableau-colorblind10')
 绘图区样式放在开头可以美化图['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight',
 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 
'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 
'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
plt.style.use()
'''

x = df['日期1']
y1 = df['第4列']
y2 = df['第5列']
plt.subplot(1, 1, 1)
plt.plot(x, y1, color='c', linestyle='solid', linewidth=1, marker='o', markersize=5, label='数据1')
plt.xlabel('X轴')
plt.ylabel('Y轴1')
plt.legend()
plt.suptitle('总表头')
# plt.twinx()  # 添加次坐标轴，一个图上两个坐标轴，双X轴用twiny，方法类似
# plt.plot(x, y2, color='m', linestyle='dashdot', linewidth=1, marker='o', markersize=5, label='数据2')
# plt.ylabel('Y轴2')
# plt.legend(loc='upper right')

# plt.subplot2grid((2, 2), (0, 0))  # 函数式添加，语句少
# x1 = df['日期1']
# y1 = df['第4列']
# plt.plot(x1, y1)
# plt.subplot2grid((2, 2), (1, 1))
# x2 = df['日期1']
# y2 = df['第6列']
# plt.bar(x2, y2)
# plt.subplot2grid((2, 2), (0, 1))
# plt.grid(True)

# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# y = np.array([12, 15, 23, 43, 48, 38, 34, 28, 10])
# colors = y * 10  # 数据点颜色
# area = y * 80  # 数据点大小
# plt.scatter(x, y, s=area, c=colors, marker='o', linewidths=1)
# for a, b in zip(x, y):  # 添加数据标签
#     plt.text(a, b, b, ha='center', va='center', fontsize=12, color='y')
# plt.title('气泡图实例')
# plt.xlabel('X轴')
# plt.ylabel('Y轴')
# plt.xlim(0, 10, 1)
# plt.ylim(0, 60, 10)
plt.grid()
plt.show()
