import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# import numpy.random.randm as randn
#
# data = pd.read_csv('E:\交通数据集\卡口识别.csv')
# data.shape
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2,3)
# plt.subplots_adjust(0, 0)
# ax1.plot(randn(1000).cumsum(), 'k')
ax2.hist([1.5, 3.5, -2, 1.5],color='k', alpha=0.3)
x = np.linspace(-np.pi, np.pi, 100)
ax1.plot(x, np.sin(x),color='g',linestyle='-',label='x1')
#插入标题
ax1.set_title('title')
#插入刻度
# ax1.set_xticklabels(['one','two','three','four','five'],rotation=30,fontsize='small')
#插入X轴名称
ax1.set_xlabel('x_name')
ax1.set_ylabel('y_name')
ax1.text(-2, 0.0, r'$\mu=100,\ \sigma=15$',family='monospace')
#设置图例位置
ax1.legend(loc='best')
x2 = np.arange(1,10)
y = x2
ax3 = fig.add_subplot(224)
# ax3.scatter([x2], [y],  facecolon = 'o')
ax3.scatter(x2, y, marker='o')
font_options={'family':'monospace','weight':'bold','size':'small'}
plt.rc('font',**font_options)
print('通过')
plt.show(1)
