
# 导入需要用到的模块
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'simhei'

# 读取目标表格文件，并用people代表读取到的表格数据
people = pd.read_excel(r'C:\Users\lxy\PycharmProjects\pythonProject\top-10.xlsx')
# x轴是类型，y轴是热度，让直方图排序显示，默认升序
people.sort_values(by='类型', inplace=True, ascending=False)
# 在控制台中输出表格数据
print(people)
# 将直方图颜色统一设置为蓝色
people.plot.bar(x='类型', y='热度', color='blue')
# 旋转X轴标签，让其横向写
plt.xticks(rotation=360)
plt.show()

