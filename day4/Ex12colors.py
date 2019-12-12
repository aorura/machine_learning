import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('ggplot')

fig, axes = plt.subplots(nrows=1,ncols=2)
ax1,ax2=axes.ravel()

data_frame=pd.DataFrame(np.random.rand(5,3),index=['Customer1','Customer2','Customer3','Customer4','Customer5'],columns=pd.Index(['Metric1','Metric2','Metric3'],name='Metrics'))

data_frame.plot(kind='bar',ax=ax1,alpha=0.75,title='Bar Plot')
plt.setp(ax1.get_xticklabels(),rotation=45,fontsize=10)
plt.setp(ax1.get_yticklabels(),rotation=0,fontsize=10)
ax1.set_xlabel('Customer')
ax1.set_ylabel('Value')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

colors = dict(boxes='DarkBlue',whiskers='Gray',medians='Red',caps='Black')
data_frame.plot(kind='box',color=colors,sym='r.',ax=ax2,title='Box Plot')
plt.setp(ax2.get_xticklabels(),rotation=45,fontsize=10)
plt.setp(ax2.get_yticklabels(),rotation=0,fontsize=10)
ax2.set_xlabel('Customer')
ax2.set_ylabel('Value')
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')

plt.savefig('pandas_plots.png',dpi=400,bbox_inches='tight')
plt.show()