import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-5, 5, 5)
y = np.ones_like(x)

fig, axes = plt.subplots(nrows = 1,ncols = 3, figsize=(12,3))

def set_axis(fig, ax, title, ymax):
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(0, ymax+1)
    ax.set_title(title)
    
linewidths = [0.5, 1.0, 2.0, 4.0]
for n, lw in enumerate(linewidths):
    axes[0].plot(x, y + n, color="blue", lw = lw)
    set_axis(fig, axes[0], "线宽", len(linewidths))
    
linestyles = ['-', '-.', ':']
for n, ls in enumerate(linestyles):
    axes[1].plot(x, y + n, color="blue", lw=2, ls = ls)
    line, = axes[1].plot(x, y + 3, color="blue", lw=2)
    length1, gap1, length2, gap2 = 10, 7, 20, 7
    line.set_dashes([length1, gap1, length2, gap2])
    set_axis(fig, axes[1], "线型", len(linestyles) + 1)
    
markersizecolors = [(4, "white"), (8, "red"), (12, "yellow"), (16, "lightgreen")]
for n, (ms, mfc) in enumerate(markersizecolors):
    axes[2].plot(x, y + n, color="blue", lw=1, ls='-',
                 marker = 'o', markersize = ms,
                 markerfacecolor = mfc, markeredgewidth = 2)
    set_axis(fig, axes[2], "标记大小/颜色", len(markersizecolors))
plt.show()
