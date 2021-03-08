import numpy as np
import seaborn as sea
import matplotlib.pyplot as plt
import pandas as pd
# 创建画布并引入axisartist工具。
import mpl_toolkits.axisartist as axisartist

np.random.seed(1)

# 创建画布
fig = plt.figure(figsize=(8, 8))
# 使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)
# 将绘图区对象添加到画布中
fig.add_axes(ax)

ax.axis[:].set_visible(False)  # 通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis["x"] = ax.new_floating_axis(0, 0)  # ax.new_floating_axis代表添加新的坐标轴
ax.axis["x"].set_axisline_style("->", size=1.0)  # 给x坐标轴加上箭头
# 添加y坐标轴，且加上箭头
ax.axis["y"] = ax.new_floating_axis(1, 0)
ax.axis["y"].set_axisline_style("-|>", size=1.0)
# 设置x、y轴上刻度显示方向
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right")

# Read original data
mul = pd.read_csv("./new4.csv")
sea.scatterplot(data=mul, x="price", y="area")
plt.xlim(-50, 50)
plt.ylim(-50, 50)
plt.show()

# 创建画布
fig = plt.figure(figsize=(8, 8))
# 使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)
# 将绘图区对象添加到画布中
fig.add_axes(ax)

ax.axis[:].set_visible(False)  # 通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis["x"] = ax.new_floating_axis(0, 0)  # ax.new_floating_axis代表添加新的坐标轴
ax.axis["x"].set_axisline_style("->", size=1.0)  # 给x坐标轴加上箭头
# 添加y坐标轴，且加上箭头
ax.axis["y"] = ax.new_floating_axis(1, 0)
ax.axis["y"].set_axisline_style("-|>", size=1.0)
# 设置x、y轴上刻度显示方向
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right")
# Read data which is lower-dimensional
X_mul = pd.read_csv("./one4.csv")
sea.scatterplot(data=X_mul, x="price", y="area")
plt.xlim(-50, 50)
plt.ylim(-50, 50)
plt.show()
