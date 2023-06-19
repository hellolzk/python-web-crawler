import numpy as np
import matplotlib.pyplot as plt

#求csv中粉丝数量总和
with open('5月27日./斗鱼直播5.27 8：00 CF.csv','r',encoding='GBK') as f:#读取csv文件
    data = np.loadtxt(f,str,delimiter=',',skiprows = 1)#读取csv
num_of_fans=data[:,3]#读取热度
top10_name8=data[:,4][0:10]#top10主播
top10_hot8=data[:,3][0:10]#top10主播热度
top10_hot8=list(top10_hot8)
new_top10_hot8 =[]
for items in top10_hot8:
    new_top10_hot8.append(float(items))
sum_fun8=0#统计热度
for item in num_of_fans:
    sum_fun8+=float(item)
num_of_rooms8=data.shape[0]#统计有几列，就说明有多少个房间


with open('5月27日./斗鱼直播5.27 12：00 CF.csv','r',encoding='GBK') as f:#读取csv文件
    data = np.loadtxt(f,str,delimiter=',',skiprows = 1)#读取csv
num_of_fans=data[:,3]#读取热度
top10_name12=data[:,4][0:10]#top10主播
top10_hot12=data[:,3][0:10]#top10主播热度
top10_hot12=list(top10_hot12)
new_top10_hot12 =[]
for items in top10_hot12:
    new_top10_hot12.append(float(items))
sum_fun12=0#统计热度
for item in num_of_fans:
    sum_fun12+=float(item)
num_of_rooms12=data.shape[0]#统计有几列，就说明有多少个房间

with open('5月27日./斗鱼直播5.27 18：00 CF.csv','r',encoding='GBK') as f:#读取csv文件
    data = np.loadtxt(f,str,delimiter=',',skiprows = 1)#读取csv
num_of_fans=data[:,3]#读取热度
top10_name18=data[:,4][0:10]#top10主播
top10_hot18=data[:,3][0:10]#top10主播热度
top10_hot18=list(top10_hot18)
new_top10_hot18 =[]
for items in top10_hot18:
    new_top10_hot18.append(float(items))
sum_fun18=0#统计热度
for item in num_of_fans:
    sum_fun18+=float(item)
num_of_rooms18=data.shape[0]#统计有几列，就说明有多少个房间

with open('5月27日./斗鱼直播5.27 22：00 CF.csv','r',encoding='GBK') as f:#读取csv文件
    data = np.loadtxt(f,str,delimiter=',',skiprows = 1)#读取csv
num_of_fans=data[:,3]#读取热度
top10_name22=data[:,4][0:10]#top10主播
top10_hot22=data[:,3][0:10]#top10主播热度
top10_hot22=list(top10_hot22)
new_top10_hot22 =[]
for items in top10_hot22:
    new_top10_hot22.append(float(items))
sum_fun22=0#统计热度
for item in num_of_fans:
    sum_fun22+=float(item)
num_of_rooms22=data.shape[0]#统计有几列，就说明有多少个房间

TIME=['8:00','12:00','18:00','22:00']#时间
sum_funs=[sum_fun8,sum_fun12,sum_fun18,sum_fun22]#热度
sum_rooms=[num_of_rooms8,num_of_rooms12,num_of_rooms18,num_of_rooms22]#房间数量


plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

plt.figure(1)
plt.title("5月27日斗鱼直播CF板块数据")#柱状图标题
plt.xlabel("时间")#X轴名称
plt.ylabel("热度/万,房间数量/个") #Y轴名称
p1=plt.bar(TIME, sum_funs, 0.2, color="red",label='热度') #绘制热度柱状图
plt.bar_label(p1, label_type='edge')#数据输出
p2=plt.bar(TIME,sum_rooms,0.2,color="yellow",label="房间数")#绘制房间数柱状图
plt.bar_label(p2, label_type='edge')#输出数据
plt.plot(TIME,sum_funs,linewidth=1,color='blue',marker='o')#绘制折线图
plt.plot(TIME,sum_rooms,linewidth=1,color='blue',marker='o')#绘制折线图
plt.legend()#显示图例
plt.show()#显示图形
plt.close()

plt.figure(2)
plt.xlabel("主播昵称")
plt.ylabel("热度")
plt.title("5月27日8:00CF板块top10")
p3=plt.bar(top10_name8, new_top10_hot8, 0.4, color="red",label='热度') #绘制柱状图
plt.xticks(top10_name8, top10_name8, rotation=20)
plt.bar_label(p3, label_type='edge')#数据输出
plt.legend()#显示图例
plt.show()#显示图形

plt.figure(3)
plt.xlabel("主播昵称")
plt.ylabel("热度")
plt.title("5月27日12:00CF板块top10")
p3=plt.bar(top10_name12, new_top10_hot12, 0.4, color="red",label='热度') #绘制柱状图
plt.xticks(top10_name12, top10_name12, rotation=20)
plt.bar_label(p3, label_type='edge')#数据输出
plt.legend()#显示图例
plt.show()#显示图形

plt.figure(4)
plt.xlabel("主播昵称")
plt.ylabel("热度")
plt.title("5月27日18:00CF板块top10")
p3=plt.bar(top10_name18, new_top10_hot18, 0.4, color="red",label='热度') #绘制柱状图
plt.xticks(top10_name18, top10_name18, rotation=20)
plt.bar_label(p3, label_type='edge')#数据输出
plt.legend()#显示图例
plt.show()#显示图形

plt.figure(5)
plt.xlabel("主播昵称")
plt.ylabel("热度")
plt.title("5月27日22:00CF板块top10")
p3=plt.bar(top10_name22, new_top10_hot22, 0.4, color="red",label='热度') #绘制柱状图
plt.xticks(top10_name22, top10_name22, rotation=20)
plt.bar_label(p3, label_type='edge')#数据输出
plt.legend()#显示图例
plt.show()#显示图形



