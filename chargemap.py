from matplotlib import pyplot as plt
import numpy as np


# 充电map函数
def chargeMap(volt, temperature):
    # 电压插值表
    voltage_table = (0, 1.5, 2.5, 2.8, 3.6, 3.9, 4)
    curr_volt_table = (0, 0, 0.03, 0.1, 1, 0.1, 0)
    # 温度插值表
    temp_table = (-20, -15, -10, -5, 0, 5, 10, 15, 20, 45, 50, 55, 60, 65)
    curr_temp_table = (0, 0, 0, 0, 0.05, 0.1, 0.2, 0.6, 1, 1, 0.6, 0.1, 0.05, 0)
    # 插值表检查
    if len(voltage_table) != len(curr_volt_table):
        print('电压插值表错误')
    if len(temp_table) != len(curr_temp_table):
        print('温度插值表错误')
    # 参数范围检查
    if volt > 4:
        volt = 4
    if volt < 0:
        volt = 0
    if temperature > 65:
        temperature = 65
    if temperature < -20:
        temperature = -20
    # 电压分段查找
    cv = 0
    for i in range(len(voltage_table) - 1):
        if voltage_table[i + 1] >= volt >= voltage_table[i]:
            cv = curr_volt_table[i + 1]
    # 温度线性插值
    ct = np.interp(temperature, temp_table, curr_temp_table)
    # print(cv, ct)
    # 过温保护
    if temperature > 60 or temperature < 0:
        ct = 0
    return min(cv, ct)


# 3D绘图数据
xx = np.arange(1.5, 4, 0.05)
yy = np.arange(-5, 65, 0.5)
zz = []
for y in yy:
    z = []
    for x in xx:
        z.append(chargeMap(x, y))
    zz.append(z)
Z = np.array(zz)
X, Y = np.meshgrid(xx, yy)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

fig = plt.figure()
ax = plt.subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=2, cstride=2, alpha=0.5, cmap=plt.get_cmap('rainbow'))
# rstride=4, cstride=4显示细腻度，太小会卡，太大有锯齿，color='b'颜色
# zdir : 'z' | 'x' | 'y' 表示把等高线图投射到哪个面, offset : 表示等高线图投射到指定页面的某个刻度
ax.contourf(X, Y, Z, zdir='x', offset=1.5)
ax.contourf(X, Y, Z, zdir='y', offset=-5)

# plt.title('充电map')
ax.set_xlabel('电压')
ax.set_xlim(1.5, 4)
ax.set_ylabel('温度')
ax.set_ylim(-5, 65)
ax.set_zlabel('充电倍率')
ax.set_zlim(0, 1.2)
ax.view_init(30, 35)
plt.show()
