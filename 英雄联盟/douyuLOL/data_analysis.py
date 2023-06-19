import pandas as pd
import matplotlib.pyplot as plt

fp = open('wordCloud.text','wt',newline='',encoding='utf-8')

df = pd.read_csv("douyuLOL.csv")  # 读取数据
df = df.sort_values(axis=0, by='popularity', ascending=False)
#print('df_loc=', df)
df.to_csv('douyuLOL',header=True,index=False)
print(df)
names = df["hostName"]
popular=df["popularity"]
plt.rcParams['figure.figsize'] = (10.0, 1.0)  # 设置图的尺寸
plt.rcParams['figure.dpi'] = 200  # 设置分辨率
# 设置图的字体
font = {
    'family': 'SimHei',
    'weight': 'bold',
    'size': '15'
}
plt.rc('font', **font)
plt.bar(names[0:5], popular[0:5])

plt.xticks(rotation=10)
plt.show()
for i in range(0,10):
    fp.writelines(names[i])
    fp.writelines(' ')
fp.close()