import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

plot_data1=np.random.randn(50).cumsum()
plot_data2=np.random.randn(50).cumsum()
plot_data3=np.random.randn(50).cumsum()
plot_data4=np.random.randn(50).cumsum()

data_frame1=pd.DataFrame(plot_data1)
data_frame2=pd.DataFrame(plot_data2)
data_frame3=pd.DataFrame(plot_data3)
data_frame4=pd.DataFrame(plot_data4)


data_frame1.plot(kind='line',ax=ax1,alpha=0.75,label='Blue Solid',marker='o', color='blue', linestyle='-')
data_frame2.plot(kind='line',ax=ax1,alpha=0.75,label='Red Dashed',marker='+', color='red', linestyle='--')
data_frame3.plot(kind='line',ax=ax1,alpha=0.75,label='Green Dash Dot',marker='*', color='green', linestyle='-.')
data_frame4.plot(kind='line',ax=ax1,alpha=0.75,label='Orange Dotted',marker='s', color='orange', linestyle=':')

plt.setp(ax1.get_xticklabels(),rotation=45,fontsize=10)
plt.setp(ax1.get_yticklabels(),rotation=0,fontsize=10)
ax1.set_xlabel('Draw')
ax1.set_ylabel('Random Number')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.legend(loc='best')
plt.show()